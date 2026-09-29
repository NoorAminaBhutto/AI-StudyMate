# 🎓 AI StudyMate

AI StudyMate is a mini Generative AI application built for a Generative AI internship practical task.

It accepts a topic or study notes and uses the Gemini API to generate:

- A concise summary
- Important key points
- Multiple-choice quiz questions
- Correct answers and short explanations

## 🧠 GenAI concepts demonstrated

1. Prompt Engineering
2. LLM/API Integration
3. Controlled/Structured Output

## 🛠️ Technologies

- Python
- Streamlit
- Google Gemini API

## 📁 Project structure

```text
AI_StudyMate/
├── app.py
├── requirements.txt
├── README.md
├── PRESENTATION_OUTLINE.md
├── LINKEDIN_POST.txt
├── RUN_INSTRUCTIONS.txt
├── .gitignore
└── .streamlit/
    ├── config.toml
    └── secrets.toml
```

## 🔐 Where do I put the API key?

Open:

```text
.streamlit/secrets.toml
```

Find:

```toml
GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"
```

Replace only `PASTE_YOUR_KEY_HERE` with your real Gemini API key.

Example:

```toml
GEMINI_API_KEY = "YOUR_REAL_KEY"
```

Do NOT put the key in `app.py`.

Do NOT commit/upload `secrets.toml` containing your real key to GitHub.

## ▶️ Run locally

Open a terminal in this project folder.

### Windows

```bash
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

If `py` does not work, try:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### macOS/Linux

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

The app normally opens at:

```text
http://localhost:8501
```

## 📸 Screenshots to take

Take screenshots of:

1. Main application
2. Entered topic and settings
3. Generated Summary + Key Points
4. Generated Quiz

Never show your API key in screenshots.

## 🚀 GitHub repository

Create a GitHub repository, for example:

`AI-StudyMate`

Upload the project files, but DO NOT upload:

```text
.streamlit/secrets.toml
```

The included `.gitignore` is already configured to prevent this.

## 🌐 Streamlit deployment

When deploying, add the secret through the deployment platform's Secrets settings rather than putting it in GitHub.

For Streamlit Community Cloud, use the app's Secrets settings and add:

```toml
GEMINI_API_KEY = "YOUR_REAL_KEY"
```

## ⚠️ If you accidentally expose an API key

Immediately revoke/rotate the exposed key from the provider and create a new one. Do not simply delete the GitHub file and assume the old key is safe.
