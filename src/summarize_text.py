import os
from dotenv import load_dotenv

# Load .env from one directory above
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

print("✅ API key loaded!")
from utils.file_ops import load_api_key, read_file, write_file

api_key = load_api_key()
text = read_file("example.txt")
write_file("output.txt", text.upper())
