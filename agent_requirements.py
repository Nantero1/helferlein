from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Based on the upper code, create a requirements.txt file.

    No version shall be freezed, so no "==1.0.0" or similar.
    After each library name, document what this library is used for and why it is needed (e.g. "requests  # for making HTTP requests").
    Do not include libraries that are not used in the code.
    Do not include second level dependencies (e.g. if you use "requests", you do not need to include "urllib3" in the requirements.txt file).
    Make sure the requirements.txt file is valid and can be used to install the libraries with pip.

    Start directly with the output of the requirements.txt file, do NOT use a code block (```) for this:
    """.strip())

OUTPUT_FILENAME = "requirements_dev.txt"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
