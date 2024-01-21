from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Erstelle eine Dokumentation im Markdown Format auf Deutsch.

    Die Dokumentation soll die Funktionen des Codes erklären.
    Die Dokumentation muss auf Deutsch sein!
    Die muss klar und verständlich sein!

    Starte direkt mit der Ausgabe der deutschen Dokumentation im Markdown Format:
    """.strip())

OUTPUT_FILENAME = "README.md"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
