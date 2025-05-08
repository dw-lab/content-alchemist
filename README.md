# Content Alchemist

Content Alchemist is a Python package designed to fetch, extract, and save content from web articles. It's particularly useful for converting online articles into structured Markdown files, making it easier to archive or process web content.

## Features

- Fetches HTML content from a given URL
- Extracts article content, including title, teaser, and main body
- Converts HTML content to Markdown format
- Handles headers, paragraphs, and image captions
- Cleans and formats text for better readability
- Saves the extracted content as a Markdown file

## Requirements

- Python 3.12 or higher
- Dependencies are automatically installed with the package

## Installation

You can install Content Alchemist directly from GitHub using pip:

```
pip install git+https://github.com/yourusername/content-alchemist.git
```

## Usage

To use Content Alchemist in your Python project, you can import and use the `ContentAlchemist` class like this:

```python
from content_alchemist import ContentAlchemist

url = "https://example.com/article"
alchemist = ContentAlchemist(url)

alchemist.fetch_content()
alchemist.extract_content()
alchemist.save_content()
```

This will create a Markdown file in the current directory with the extracted content.

## Class: ContentAlchemist

### Methods

- `__init__(self, url)`: Initializes the ContentAlchemist with a given URL.
- `fetch_content(self)`: Fetches the HTML content from the URL.
- `extract_content(self)`: Extracts and formats the content from the fetched HTML.
- `save_content(self)`: Saves the extracted content as a Markdown file.
- `get_title(self)`: Extracts the title from the HTML content.
- `clean_text(text)`: Static method to clean and format text.

## Error Handling

The package includes error handling and logging for various scenarios:

- Network errors when fetching content
- Missing article or content elements in the HTML
- File I/O errors when saving content

Errors and informational messages are logged using Python's built-in logging module.

## Contributing

Contributions to Content Alchemist are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
