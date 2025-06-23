import google.generativeai as genai
from utils.file_ops import load_api_key

def convert_to_markdown(input_file="extracted_text.txt", output_file="output.md"):
    # Load API key and configure
    api_key = load_api_key()
    if not api_key:
        print("Gemini API Key not found!")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    # Read extracted text
    with open(input_file, "r", encoding="utf-8") as file:
        raw_text = file.read()

    # Prompt Gemini to convert to Markdown
    prompt = f"""
    Convert the following extracted PDF text to clean, readable Markdown:
    Preserve structure like headers, bullet points, code blocks, etc.
    
    Text:
    {raw_text}
    """

    response = model.generate_content(prompt)
    markdown_text = response.text

    # Save as .md file
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(markdown_text)

    print(f"✅ Markdown file created: {output_file}")

if __name__ == "__main__":
    convert_to_markdown()
