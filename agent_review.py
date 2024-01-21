from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Mache ein Review des Codes auf Deutsch nach folgenden Kriterien:
    
    - Ist der Code verständlich?
    - Ist der Code gut strukturiert?
    - Ist der Code gut formatiert?
    - Ist der Code gut lesbar?
    - Ist der Code gut wartbar?
    - Ist der Code gut erweiterbar?
    - Ist der Code gut testbar?
    - Sind komplexe Codeteile gut kommentiert?
    - Ist ein roter Faden erkennbar?
    - Sind die Klassen, Variablen und Funktionen gut benannt?
    
    Mache eine Bewertung von 1 bis 10, wobei 1 sehr schlecht ist und 10 sehr gut ist für jeden der Punkte.
    Mache eine Gesamtbewertung von 1 bis 10, wobei 1 sehr schlecht ist und 10 sehr gut ist.
    Schlage Verbesserungen vor, um die Bewertung zu erhöhen, 
    zitiere dabei den Originalcode und gebe verbesserten Code aus.
    
    Nutze Markdown, Codeblöcke und emojis, um die Bewertung und Verbesserungsvorschläge zu formatieren.
    
    Starte direkt mit der Bewertung und Verbesserungsvorschlägen, wie besprochen:
    """.strip())

OUTPUT_FILENAME = "review.md"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
