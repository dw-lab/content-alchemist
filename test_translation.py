from materia_laboris.content_processor import ContentProcessor
from materia_laboris.language_detector import LanguageDetector
from materia_laboris.langgraph_translator import LanggraphTranslator
import requests


def test_content_processor():
    url = "https://www.dw.com/de/bilanz-nach-100-tagen-präsident-trump-usa-im-wirbelwind/a-72356648"
    response = requests.get(url)
    processor = ContentProcessor()
    content = processor.extract_content(response.text)
    print("Extracted content:")
    print(content[:500] + "...")  # Print first 500 characters


def test_language_detector():
    detector = LanguageDetector()
    test_text = "Ovo je test na bosanskom jeziku."
    language = detector.detect_language(test_text)
    print(f"Detected language: {language}")


def test_translator():
    translator = LanggraphTranslator()
    test_text = "Ovo je test prijevoda."
    source_language = "Bosnian"
    translations = translator.translate(test_text, source_language)
    print("Translations:")
    for lang, translation in translations.items():
        print(f"{lang}: {translation}")


if __name__ == "__main__":
    print("Testing Content Processor:")
    test_content_processor()
    print("\nTesting Language Detector:")
    test_language_detector()
    print("\nTesting Translator:")
    test_translator()
