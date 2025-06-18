def load_api_key(filepath="../.env"):
    with open(filepath, "r") as file:
        for line in file:
            if line.startswith("OPENAI_API_KEY="):
                return line.strip().split("=")[1]
    raise ValueError("API key not found in .env file")


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
