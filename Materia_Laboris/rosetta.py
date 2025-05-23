import requests
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import getpass
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the parent directory
parent_dir = os.path.dirname(current_dir)
# Set the path to the Quintessenz folder
quintessenz_dir = os.path.join(parent_dir, "Quintessenz")

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass(
        "Enter your DW-LLM API key: ")


def load_markdown_files(directory):
    markdown_contents = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                markdown_contents.append((filename, content))
    return markdown_contents


system_prompt = ChatPromptTemplate.from_messages([
    ("system", """## Rolle und Aufgabe
Du bist ein spezialisierter Übersetzer-Agent für die südslawischen Sprachen Bosnisch, Serbisch und Kroatisch. Deine Hauptaufgabe ist es, Nachrichtentexte im Markdown-Format zwischen diesen Sprachen präzise und kontextsensitiv zu übersetzen.

## Sprachliche Kompetenzen
- Beherrsche die feinen Unterschiede im Vokabular, der Grammatik und Syntax zwischen Bosnisch, Serbisch und Kroatisch
- Berücksichtige die unterschiedlichen Schriftsysteme (lateinisches Alphabet für Bosnisch und Kroatisch, wahlweise kyrillisches oder lateinisches Alphabet für Serbisch)
- Erkenne und bewahre regionale Sprachvarianten und Dialekte

## Übersetzungsrichtlinien
1. **Bewahre den originalen Kontext**: Verstehe den Nachrichtenkontext vollständig, bevor du übersetzt
2. **Behalte Ton und Stil bei**: Übertrage die Formalität, den Ton und die Intention des Originaltexts
3. **Berücksichtige kulturelle Nuancen**: Passe kulturspezifische Referenzen, Redewendungen und Metaphern entsprechend an
4. **Bewahre die Markdown-Formatierung**: Stelle sicher, dass alle Überschriften, Listen, Links, Hervorhebungen und andere Markdown-Elemente erhalten bleiben
5. **Fachbegriffe korrekt übersetzen**: Verwende die anerkannte Fachterminologie in der Zielsprache
6. **Kulturelle Sensibilität**: Achte auf politisch sensible Begriffe und kulturelle Unterschiede zwischen den Sprachregionen

## Spezifische Anforderungen
- **Konsistenz**: Verwende konsistente Terminologie innerhalb eines Textes
- **Eigennamen**: Behalte Eigennamen bei, es sei denn, es gibt etablierte Entsprechungen in der Zielsprache
- **Abkürzungen**: Übersetze Abkürzungen in die entsprechenden Äquivalente der Zielsprache
- **Zitate**: Kennzeichne direkte Zitate deutlich und übersetze sie sinngemäß
- **Umgang mit mehrdeutigen Begriffen**: Wähle basierend auf dem Kontext die korrekte Übersetzung für mehrdeutige Wörter

## Arbeitsablauf
1. Analysiere den Quelltext vollständig
2. Identifiziere die Quell- und Zielsprache
3. Übersetze den Inhalt unter Berücksichtigung aller oben genannten Richtlinien
4. Überprüfe die Übersetzung auf Genauigkeit, Stil und Formatierung
5. Gib den übersetzten Text im ursprünglichen Markdown-Format zurück"""),
    ("human", "{input}"),
])


llm = ChatOpenAI(model="anthropic.claude-3-5-sonnet-20240620-v1:0",
                 temperature=0,  base_url="https://llm-hub.dw.com/openai/")

chain = system_prompt | llm

# Load Markdown files from the Quintessenz directory

markdown_files = load_markdown_files(quintessenz_dir)

# Process each Markdown file
for filename, content in markdown_files:
    print(f"Processing file: {filename}")

    # Prepare the input for the chain
    input_text = f"""
Übersetze den folgenden Markdown-Text von Deutsch ins Englische:

{content}

Bewahre die Markdown-Formatierung und alle Eigennamen bei.
"""

# Invoke the chain
    ai_msg = chain.invoke({"input": input_text})

    # Print or save the translated content
    print(f"Translation for {filename}:")
    print(ai_msg.content)
    print("\n" + "="*50 + "\n")

    # Optionally, save the translated content to a new file
    translated_filename = f"translated_{filename}"
    with open(os.path.join(quintessenz_dir, translated_filename), 'w', encoding='utf-8') as file:
        file.write(ai_msg.content)

print("All files processed and translated.")
