import sys
import os

# Step 1: Get file path from command-line
if len(sys.argv) < 2:
    print("[ERROR] Please provide the PDF file path as an argument.")
    print("Usage: python main.py your_file.pdf")
    exit()

file_path = sys.argv[1]

# Step 2: Validate file existence and extension
if not os.path.exists(file_path):
    print(f"[ERROR] File '{file_path}' does not exist.")
    exit()

if not file_path.lower().endswith(".pdf"):
    print("[ERROR] Only PDF files are supported.")
    exit()

from pdf_reader import convert_pdf_to_text
from markdown_converter import convert_text_to_markdown
from gemini_formatter import enhance_markdown_with_gemini
import os

# ===== STEP 1: Input Validation =====
file_path = "sample.pdf1.pdf"
if not os.path.exists(file_path):
    print("[ERROR] File does not exist.")
    exit()
if not file_path.endswith(".pdf"):
    print("[ERROR] Only PDF files are supported.")
    exit()

# ===== STEP 2: PDF to Text Conversion with Error Handling =====
try:
    text = convert_pdf_to_text(file_path)
except FileNotFoundError:
    print("[ERROR] PDF file not found.")
    exit()

if not text.strip():
    print("[ERROR] PDF appears empty. Please check the file.")
    exit()

# ===== STEP 3: Text to Markdown Conversion =====
try:
    markdown_text = convert_text_to_markdown(text)
except Exception as e:
    print(f"[ERROR] Markdown conversion failed: {e}")
    exit()

# ===== STEP 4: Enhance with Gemini AI (Optional) =====
try:
    ai_markdown = enhance_markdown_with_gemini(markdown_text)
except Exception as e:
    print(f"[WARNING] Gemini enhancement failed: {e}")
    ai_markdown = markdown_text  # Fallback

# ===== STEP 5: Save Output =====
output_file = "ai_output.md"
if os.path.exists(output_file):
    print("[INFO] Overwriting existing ai_output.md")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(ai_markdown)

print("✅ Gemini-enhanced Markdown saved to ai_output.md")
