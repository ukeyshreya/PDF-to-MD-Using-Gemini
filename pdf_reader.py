from PyPDF2 import PdfReader

def convert_pdf_to_text(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        print(f"[ERROR] Failed to read PDF: {e}")
        return ""
