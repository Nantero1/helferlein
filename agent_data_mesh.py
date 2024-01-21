from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Given the upper code, consider the principles of data mesh and suggest improvements.
    
    Consider the following (list not complete):
    
    - use of proper data domains
    - make sure data which might be relevant for Machine Learning and Data Scientist is made available
    - which data might be relevant for others? Suggest code improvements to make it available to others
    - if valuable data is processed, suggest how this data might be stored and which fields might be relevant
    - explain why you think this data might be relevant for others 
    
    Start directly with the suggestions, use markdown, use code blocks (```) for code suggestions:
    """.strip())

OUTPUT_FILENAME = "data_mesh.md"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
