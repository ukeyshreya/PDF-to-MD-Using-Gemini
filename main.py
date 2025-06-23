from pdf_reader import extract_text_from_pdf
from markdown_converter import convert_text_to_markdown  # NEW import

if __name__ == "__main__":
    input_pdf = "sample.pdf1.pdf"  # use your actual PDF filename
    text = extract_text_from_pdf(input_pdf)

    # Save raw extracted text
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # Convert to Markdown
    markdown = convert_text_to_markdown(text)

    # Save as Markdown file
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    print("✅ PDF converted to Markdown successfully.")

