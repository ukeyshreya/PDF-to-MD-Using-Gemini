import fitz  # PyMuPDF
import os

# Step 1: Give your PDF file name here
pdf_file = "sample.pdf1.pdf"  # 🔁 Replace with your actual PDF file name

# Step 2: Open the PDF file
if not os.path.exists(pdf_file):
    print("❌ PDF file not found!")
    exit()

doc = fitz.open(pdf_file)

# Step 3: Extract text from each page
all_text = ""
for page in doc:
    text = page.get_text()
    all_text += text + "\n\n"

doc.close()

# Step 4: Save the text to a file
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("✅ Text extracted and saved to extracted_text.txt")
