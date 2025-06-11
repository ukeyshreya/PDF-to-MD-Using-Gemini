
def main():
    print("\n📄 PDF to Markdown Converter - File Selection Step")

    pdf_files = list_pdf_files()
    selected_file = select_pdf_file(pdf_files)

    print(f"\n✅ You selected: {selected_file}")
    print("\n🔍 Extracting content...\n")

    content = extract_text_from_pdf(selected_file)
    print(content[:1000]) # print first 1000 characters

    # Save content to markdown
    output_file = selected_file.replace(".pdf", ".md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Markdown file saved as: {output_file}")

    import PyPDF2
import os

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

if __name__ == '__main__':
    pdf_file = '../file-sample.pdf'  # use correct path if inside src
    if os.path.exists(pdf_file):
        text = extract_text_from_pdf(pdf_file)
        print(text)
    else:
        print("❌ PDF file not found. Place 'file-sample.pdf' in project folder.")
