def generate_summary_with_gemini(text):
    # Limit input to first 1000 characters (~150-200 words)
    short_text = text[:1000]

    prompt = (
        "Summarize the following text in 5-6 bullet points with a heading '## Summary':\n\n" + short_text
    )

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Switch to a lighter model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"[WARNING] Summary generation failed: {e}")
        return "## Summary\n- Summary not available."
print("✅ Processing complete. Output saved to summary_output.md")
