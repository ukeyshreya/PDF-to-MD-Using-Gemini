from pdf_reader import extract_text_from_pdf
from markdown_converter import convert_text_to_markdown
from gemini_formatter import enhance_markdown_with_gemini

if __name__ == "__main__":
    input_pdf = "sample.pdf1.pdf"
    text = extract_text_from_pdf(input_pdf)

    # Save plain extracted text
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # Convert to basic markdown
    markdown = convert_text_to_markdown(text)
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    # Send to Gemini for better formatting
    ai_markdown = enhance_markdown_with_gemini(text)
    with open("ai_output.md", "w", encoding="utf-8") as f:
        f.write(ai_markdown)

    print("✅ Gemini-enhanced Markdown saved to ai_output.md")
