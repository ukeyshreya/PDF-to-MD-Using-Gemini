from utils.file_ops import read_file, write_file

# Read summarized text from summary.txt
summary = read_file("summary.txt")  # Make sure this file exists

# Convert to Markdown format
markdown_text = f"# Summary\n\n{summary}"

# Write to summary.md file
write_file("summary.md", markdown_text)

print("✅ Markdown file created successfully!")
