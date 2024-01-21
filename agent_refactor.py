from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Given the upper code, consider the principles of clean code and refactor the code.
    Consider the following (list not complete):
    
    - use of proper naming
    - use of proper comments
    - use of proper functions
    - use of proper classes
    - use of proper modules
    - use of proper packages
    - use of proper interfaces
    - use of proper inheritance
    - use of proper composition
    - use of proper abstraction
    - use of proper encapsulation
    - use of proper coupling
    - use of proper cohesion
    - use of proper design patterns
    - use of proper SOLID principles
    - use of proper DRY principle
    - use of proper KISS principle
    - use of proper YAGNI principle
    - use of proper code formatting and literate programming
    - use of proper code documentation and docstrings with numpydoc
    - you may split the code into multiple files
    
    Start directly with the refactored code, use markdown, use code blocks (```) and in case you use multiple files, 
    give them proper names and use the proper file extension (e.g. .py for python files):
    """.strip())

OUTPUT_FILENAME = "refactored.md"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
