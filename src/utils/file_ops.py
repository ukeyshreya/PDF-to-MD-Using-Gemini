from dotenv import load_dotenv
import os

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("❌ API key not found. Check your .env file!")
    return api_key

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
