import re
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class ContentAlchemist:
    def __init__(self, url):
        self.url = url
        self.raw_html = None
        self.extracted_content = None

    def fetch_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.raw_html = response.text
            logging.info(f"Content fetched successfully from {self.url}")
        except requests.RequestException as e:
            logging.error(f"Error fetching content: {e}")
            raise

    def extract_content(self):
        if not self.raw_html:
            raise ValueError(
                "No HTML content to extract. Call fetch_content() first.")

        soup = BeautifulSoup(self.raw_html, 'html.parser')
        article = soup.find('article')

        if not article:
            logging.warning("No article found in the HTML content.")
            return "No article found in the HTML content."

        header = article.find("header")
        teaser_text = header.find("p", class_="teaser-text").get_text()
        teaser_text = f"### {teaser_text}"

        rich_text_div = article.find('div', class_='rich-text')

        if not rich_text_div:
            logging.warning("No rich-text div found within the article.")
            return "No rich-text div found within the article."

        content = ["# " + self.get_title() + "\n" + teaser_text + "\n"]
        for element in rich_text_div.children:
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                content.append(f"\n## {self.clean_text(element.get_text())}\n")
            elif element.name == 'p':
                content.append(self.clean_text(element.get_text()))
            elif element.name == 'figure':
                img_caption = element.find('figcaption')
                if img_caption:
                    caption_text = self.clean_text(img_caption.get_text())
                    caption_text = re.sub(r'^Bild:\s*', '', caption_text)
                    content.append(f"\n*{caption_text}*\n")

        self.extracted_content = '\n\n'.join(content)
        self.extracted_content = re.sub(
            r'\n{3,}', '\n\n', self.extracted_content)
        logging.info("Content extracted successfully")

    def save_content(self):
        filename = f"{self.get_title()}.md"
        if not self.extracted_content:
            raise ValueError(
                "No extracted content to save. Call extract_content() first.")

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.extracted_content)
            logging.info(f"Content saved successfully to {filename}")
        except IOError as e:
            logging.error(f"Error saving content: {e}")
            raise

    def get_title(self):
        if not self.raw_html:
            raise ValueError("No HTML content. Call fetch_content() first.")

        soup = BeautifulSoup(self.raw_html, 'html.parser')
        title = soup.find('title')
        return self.clean_text(title.string) if title else "Untitled"

    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'<[^>]+>', '', text)
        return text
