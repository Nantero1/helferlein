from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Given the upper code, write unit tests using for each function.
    
    If it is Python code, use pytest and a structure like this:
    
    ```python
    import pytest
    
    from main import example_function
    
    def test_example_function():
        # given:
        input = "some input"
        
        # when:
        output = example_function(input)
        
        # then:
        assert output == "some expected output", "output is not as expected"
    ```
    
    If is is not Python code, use the unit test framework of the language.
    
    Start directly with the output of the unit tests, do NOT use a code block (```) for this,
    make it a valid file that can be executed with the unit test framework of the language:
    """.strip())

OUTPUT_FILENAME = "tests.py"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
