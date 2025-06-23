from pdf_reader import extract_text_from_pdf

if __name__ == "__main__":
    input_pdf = "sample.pdf1.pdf"  # You can change this to any of your actual files
    text = extract_text_from_pdf(input_pdf)

    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ PDF text extraction complete.")
