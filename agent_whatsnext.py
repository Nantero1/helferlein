from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Schlagen Sie anhand des oberen Codes neue Funktionen vor, die den Code erweitern könnten.
    Schlagen Sie vor, was als nächstes getan werden könnte und warum es nützlich wäre.
    Verwenden Sie typische agile User Stories.
    Verwenden Sie Markdown und emojis, um die User Stories zu formatieren.
    
    Starten Sie direkt mit den User Stories, wie besprochen, verwenden Sie dafür KEINEN Codeblock (```)!
    """.strip())

OUTPUT_FILENAME = "whatsnext.md"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
