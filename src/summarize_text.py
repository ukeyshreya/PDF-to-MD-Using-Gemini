from utils.file_ops import load_api_key, read_file, write_file
import openai

# ✅ Load API Key
api_key = load_api_key()
print("✅ API key loaded!")

# ✅ Load example text
text = read_file("example.txt")

# ✅ Set API key for OpenAI
openai.api_key = api_key

# ✅ Make API call
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Summarize the following text."},
        {"role": "user", "content": text}
    ]
)

summary = response["choices"][0]["message"]["content"]

# ✅ Write summary to file
write_file("summary.txt", summary)

