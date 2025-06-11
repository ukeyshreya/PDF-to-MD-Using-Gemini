# PDF to MarkDown Using LLM (Gemini)

This project is based on converting small PDFs to Markdown file format using LLM with custom formatting options.

## What is in this repo?

This repository contains basic project structure, requirements, and this README.

## How to setup?

**Remember to fork this repository and work in that repository only. All commits and pushed will be done to your own forked repo, and not this.** \
**OR** \
**Use this template to create a new repo**

1. First create a virtual environment. If you don't know how to do that, below are the basic commands: \
   _Use Python 3.13 or greater_. \
   _Do not use CMD.exe on Windows. Use Powershell_

```bash
python -m venv .venv
```

2. Then activate the virtual environment using:

```bash
.\.venv\Scripts\Activate.ps1    # For Windows Powershell.

source .venv/bin/activate       # For Linux and macOS.
```

Read more about virtual environments here: https://docs.python.org/3/library/venv.html

3. Next install the requirements from `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Now your project is setup and ready to be worked on.

## How to approach this project?

This project has the following goals:

- Create a CLI UI to select .pdf files to be converted in current directory.
- Create a new directory named `<current-directory>_converted-md`.
- Store all converted .md files in the newly created directory

Use the bundled modules:

- Google Genai
- Inquirer

The stepwise process of how the application will work is:

1. New directory is created.
2. User will select files using inquirer.
3. The application will take those files and send them to gemini one by one.
4. The response is to be stored in a file with .md extension with same name as the .pdf file.
5. The .md files will be stored in the created directory.

## Things to keep in mind:

- _NO AI CODE SHALL BE USED._ Any plagarised or code given by LLMs can be detected. Anyone found using these tactics will be barred from receiving the completion certificate.
- _NO CODE SHARING_. Every intern must have their own unique code and project style. Same rules as above for violation of this rule.
- Any number of files can be created depending on the neccesity and use.
- Do not clutter the main.py file, try and create multiple files for different logic sections (Eg: converter.py handle the conversion using gemini, filesystem_update.py creates and updated directories and files in filesystem).
# PDF to Markdown Converter using Gemini API

This project converts PDF content to Markdown using the Gemini AI API.

## Features
- Upload PDF file
- Extract text
- Convert to Markdown using Gemini
- Save converted file

## Setup Instructions

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
pip install -r requirements.txt
python src/main.py
GEMINI_API_KEY=your_api_key_here




