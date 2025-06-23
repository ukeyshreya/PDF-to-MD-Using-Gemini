from utils.file_ops import read_file, write_file

# Step 1: Read from summary.txt
summary = read_file("summary.txt")

# Step 2: Add Markdown formatting
markdown = f"# Summary\n\n{summary}"

# Step 3: Write to summary.md
write_file("summary.md", markdown)

print("✅ Converted summary.txt to summary.md")
