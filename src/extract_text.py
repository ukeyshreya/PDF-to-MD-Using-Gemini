import fitz  # PyMuPDF
import os
pdf_file = "sample.pdf1.pdf"  # 🔁 Replace with your actual PDF file name
if not os.path.exists(pdf_file):
    print("❌ PDF file not found!")
    exit()
doc = fitz.open(pdf_file)
all_text = ""
for page in doc:
    text = page.get_text()
    all_text += text + "\n\n"
doc.close()
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(all_text)
print("✅ Text extracted and saved to extracted_text.txt")

