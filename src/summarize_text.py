from transformers import pipeline
from utils.file_ops import read_file, write_file

# ✅ Load the text
text = read_file("example.txt")
print("✅ Text loaded!")

# ✅ Initialize the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ✅ Summarize
summary_list = summarizer(text, max_length=150, min_length=40, do_sample=False)
summary = summary_list[0]['summary_text']

# ✅ Write summary to file
write_file("summary.txt", summary)
print("✅ Summary written to summary.txt")
