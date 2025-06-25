import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Use correct model name format
model = genai.GenerativeModel("models/gemini-1.5-flash")



def enhance_markdown_with_gemini(text):
    prompt = f"""
You are a Markdown formatting assistant. 
Take the following plain text extracted from a PDF and convert it into well-formatted Markdown. 
Apply headings, subheadings, bold where appropriate, and preserve lists and tables.

Text:
{text}
"""
    response = model.generate_content(prompt)
    return response.text

def generate_summary_with_gemini(text):
    prompt = (
        "Summarize the following text in 5-6 bullet points with a heading '## Summary':\n\n" + text
    )
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"[WARNING] Summary generation failed: {e}")
        return "## Summary\n- Summary not available."
