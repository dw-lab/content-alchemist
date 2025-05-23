import re
import requests
import logging
import os
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class QuintessenzAkkumulator:
    def __init__(self, url):
        self.urls: list[str] = url
        self.raw_html: list[str] = []
        self.extracted_content: list[str] = []

    def fetch_content(self):
        for url in self.urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                self.raw_html.append(response.text)
                logging.info(f"Content fetched successfully from {url}")
            except requests.RequestException as e:
                logging.error(f"Error fetching content: {e}")
                raise

    def extract_content(self):
        for index, raw_html in enumerate(self.raw_html):
            if not raw_html:
                logging.warning(
                    f"No HTML content to extract for item {index}. Skipping.")
                continue

            soup = BeautifulSoup(raw_html, 'html.parser')
            article = soup.find('article')

            if not article:
                logging.warning(
                    f"No article found in the HTML content for item {index}. Skipping.")
                continue

            header = article.find("header")
            teaser_text = header.find("p", class_="teaser-text")
            if teaser_text:
                teaser_text = f"### {teaser_text.get_text()}"
            else:
                teaser_text = ""

            rich_text_div = article.find('div', class_='rich-text')

            if not rich_text_div:
                logging.warning(
                    f"No rich-text div found within the article for item {index}. Skipping.")
                continue

            title = soup.find('title')
            title_text = self.clean_text(title.string) if title else "Untitled"
            content = [f"# {title_text}\n{teaser_text}\n"]
            for element in rich_text_div.children:
                if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    content.append(
                        f"\n## {self.clean_text(element.get_text())}\n")
                elif element.name == 'p':
                    content.append(self.clean_text(element.get_text()))
                elif element.name == 'figure':
                    img_caption = element.find('figcaption')
                    caption_text = ""
                    if img_caption:
                        caption_text = self.clean_text(img_caption.get_text())
                        content.append(f"\n*{caption_text}*\n")

            article_content = '\n\n'.join(content)
            article_content = re.sub(r'\n{3,}', '\n\n', article_content)
            self.extracted_content.append(article_content)
            logging.info(f"Content extracted successfully for item {index}")

    def save_content(self, folder_name: str | None = None):
        folder_name = folder_name or "Quintessenz"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        if not self.extracted_content:
            raise ValueError(
                "No extracted content to save. Call extract_content() first.")
        for index, content in enumerate(self.extracted_content):
            title = self.get_title(content)
            filename = f"{title}_{index}.md"
            file_path = os.path.join(folder_name, filename)
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                logging.info(f"Content saved successfully to {file_path}")
            except IOError as e:
                logging.error(f"Error saving content for item {index}: {e}")
                raise
        logging.info(f"All content saved in folder {folder_name}")

    def get_title(self, content):
        if not content:
            return "Untitled"

        # Extract title from the markdown content
        title_match = re.search(r'^# (.+)', content, re.MULTILINE)
        if title_match:
            return self.clean_text(title_match.group(1))
        else:
            return "Untitled"

    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'<[^>]+>', '', text)
        return text
