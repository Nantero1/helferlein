import os
from hashlib import md5
from random import randint
from time import sleep

from dotenv import load_dotenv
from langchain.globals import set_debug
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# change as needed
PROJECT_FILE_PATH = "<REPLACE WITH PATH TO PROJECT>"
PROJECT_MAIN_FILE = "main.py"


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def run_agent(code, prompt):
    model = ChatOpenAI(model="gpt-4-1106-preview")
    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    chain_output = chain.invoke({"code": code})
    print(chain_output)

    return chain_output


def create_output_by_agent(prompt, output_filename):
    # setup
    set_debug(True)
    load_dotenv()

    file_md5 = None
    while True:  # noqa
        # load agent input
        input_file_path = os.path.join(PROJECT_FILE_PATH, PROJECT_MAIN_FILE)
        file_content = read_file(input_file_path)

        # check if file changed and if run is needed
        file_md5_new = md5(file_content.encode("utf-8")).hexdigest()
        if file_md5_new == file_md5:
            print("No changes detected, skipping agent run.")
            sleep(20 + randint(0, 5))
            continue
        file_md5 = file_md5_new

        # run agent
        markdown_output = run_agent(code=file_content, prompt=prompt)

        # store agent output
        output_file_path = os.path.join(PROJECT_FILE_PATH, output_filename)
        write_file(output_file_path, markdown_output)

        # wait 20-30 seconds, to not cause too much load on the API and locks
        sleep(20 + randint(0, 5))
