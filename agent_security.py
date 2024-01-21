from langchain_core.prompts import ChatPromptTemplate

from common import create_output_by_agent

PROMPT = ChatPromptTemplate.from_template(
    """
    ```python
    {code}
    ```
    Is the code secure? If not, what could be done to make it more secure?
    
    Consider the following (list not complete):
    - SQL injection
    - Cross-site scripting
    - Cross-site request forgery
    - Session hijacking
    - Brute force attacks
    - Denial of service attacks
    - Eavesdropping
    - Phishing
    - Clickjacking
    - Cookie theft
    - use of proper encryption
    - use of proper hashing
    - use of proper encoding
    - use of proper escaping
    - use of proper sanitizing
    - use of proper validation
    - use of proper authentication
    - use of proper authorization
    - use of proper access control
    - use of proper logging
    - use of proper error and exception handling
    - use of proper exception handling
    - use of proper libraries for security and not implementing it yourself
    - focus also on other security aspects not mentioned here
    
    Rate the security from 1 to 10, where 1 is very insecure and 10 is very secure.
    Give reasons for your rating and suggestions for improvement, cite the original code and give improved code.
    Use Markdown and emojis to format the rating and reasons.
    
    Start directly with the rating and reasons, use markdown, as discussed, do NOT use a code block (```) for this:
    """.strip())

OUTPUT_FILENAME = "security.md"


def main():
    create_output_by_agent(prompt=PROMPT, output_filename=OUTPUT_FILENAME)


if __name__ == '__main__':
    main()
