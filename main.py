from materia_laboris.akkumulator import QuintessenzAkkumulator
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    urls = [
        "https://www.dw.com/de/auflösung-der-pkk-hoffnung-auf-frieden/a-71768696",

    ]

akkumulator = QuintessenzAkkumulator(urls)

akkumulator.fetch_content()


akkumulator.extract_content()
akkumulator.save_content()
