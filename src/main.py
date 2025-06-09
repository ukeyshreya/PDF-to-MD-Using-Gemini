import os
import inquirer
import fitz  # PyMuPDF

def list_pdf_files():
    files = [f for f in os.listdir() if f.lower().endswith(".pdf")]
    if not files:
        print("❌ No PDF files found in this folder.")
        exit()
    return files

def select_pdf_file(files):
    questions = [
        inquirer.List('file', message="Select a PDF file", choices=files)
    ]
    answer = inquirer.prompt(questions)
    return answer['file']

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
        return full_text
    except Exception as e:
        return f"❌ Error reading PDF: {e}"

def main():
    print("\n📄 PDF to Markdown Converter - File Selection Step")

    pdf_files = list_pdf_files()
    selected_file = select_pdf_file(pdf_files)

    print(f"\n✅ You selected: {selected_file}")
    print("\n🔍 Extracting content...\n")

    content = extract_text_from_pdf(selected_file)
    print(content[:1000])  # print first 1000 characters

if __name__ == "__main__":
    main()
