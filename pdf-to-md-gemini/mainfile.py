from pdf_reader import extract_text_from_pdf

if __name__ == "__main__":
    input_pdf = "pdfs/pdf_file1.pdf"
    text = extract_text_from_pdf(input_pdf)

    with open("output/sample_output.txt", "w") as f:
        f.write(text)

    print("PDF text extraction complete.")
