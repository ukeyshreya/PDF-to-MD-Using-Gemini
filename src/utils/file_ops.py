import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY")

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        return file.read()


def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

