def convert_text_to_markdown(text):
    lines = text.split("\n")
    md_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            md_lines.append("")  # preserve blank lines
            continue

        # Headings: if line is in uppercase and short → treat as title
        if line.isupper() and len(line.split()) < 6:
            md_lines.append(f"# {line.title()}")
        
        # Bullet points
        elif line.startswith("- ") or line.startswith("• "):
            md_lines.append(f"- {line[2:]}")
        
        # Just a normal paragraph
        else:
            md_lines.append(line)

    return "\n".join(md_lines)
