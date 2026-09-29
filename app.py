import streamlit as st
from google import genai

# ============================================================
# AI StudyMate - Mini Generative AI Application
# ============================================================
# API KEY LOCATION:
# Paste your Gemini API key ONLY in:
# .streamlit/secrets.toml
#
# Example:
# GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"
#
# DO NOT paste the API key into this Python file.
# DO NOT upload secrets.toml to GitHub.
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🎓",
    layout="centered",
)

st.title("🎓 AI StudyMate")
st.caption("AI-powered study notes and quiz generator")

with st.sidebar:
    st.header("⚙️ Settings")
    difficulty = st.selectbox(
        "Difficulty level",
        ["Beginner", "Intermediate", "Advanced"],
        index=1,
    )
    num_questions = st.slider(
        "Number of quiz questions",
        min_value=3,
        max_value=10,
        value=5,
    )
    st.divider()
    st.info(
        "🔐 API key setup:\n\n"
        "Open `.streamlit/secrets.toml` and replace "
        "`PASTE_YOUR_KEY_HERE` with your Gemini API key."
    )

st.markdown(
    """
Enter a topic or paste your study notes below. The application will use
Generative AI to create a summary, key points, and multiple-choice questions.
"""
)

notes = st.text_area(
    "📚 Topic / Study Notes",
    height=240,
    placeholder=(
        "Example:\n"
        "Artificial Intelligence is the field of creating systems that can "
        "perform tasks normally associated with human intelligence..."
    ),
)

generate = st.button("✨ Generate Study Material", type="primary", use_container_width=True)

if generate:
    if not notes.strip():
        st.warning("Please enter a topic or some study notes first.")
        st.stop()

    # Read the secret safely from Streamlit.
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        st.error(
            "Gemini API key is not configured. Open "
            "`.streamlit/secrets.toml` and add your API key."
        )
        st.stop()

    if not api_key or api_key == "PASTE_YOUR_KEY_HERE":
        st.error(
            "Your Gemini API key is missing. Paste it into "
            "`.streamlit/secrets.toml`."
        )
        st.stop()

    prompt = f"""
You are an expert educational AI assistant.

Create study material from the user's notes below.

USER NOTES:
{notes}

DIFFICULTY:
{difficulty}

NUMBER OF QUESTIONS:
{num_questions}

IMPORTANT INSTRUCTIONS:
1. Use the supplied notes as the primary source.
2. Do not invent unsupported facts.
3. Use clear language appropriate for the selected difficulty.
4. Make the output easy for a student to study.
5. Follow the exact structure below.

## 1. Summary
Write a concise but useful summary.

## 2. Key Points
Give 5 to 8 important points as bullet points.

## 3. Quiz
Create exactly {num_questions} multiple-choice questions.
For each question:
- Provide four options: A, B, C, D.
- Clearly state the correct answer.
- Give a short explanation for the answer.

This is an educational application, so prioritize accuracy and clarity.
"""

    with st.spinner("🤖 Generating your study material..."):
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )

            result = response.text

            if not result:
                st.error("The AI returned an empty response. Please try again.")
                st.stop()

            st.success("✅ Study material generated successfully!")

            st.markdown(result)

            st.download_button(
                label="⬇️ Download Study Material",
                data=result,
                file_name="ai_studymate_result.txt",
                mime="text/plain",
                use_container_width=True,
            )

        except Exception as exc:
            st.error("The AI request could not be completed.")
            st.code(str(exc))
            st.info(
                "Check that your API key is correct, active, and that "
                "the required package is installed."
            )

st.divider()
st.markdown(
    """
### 🧠 GenAI Concepts Demonstrated
- **Prompt Engineering:** A structured prompt controls the role, task,
  difficulty, number of questions, and output format.
- **LLM API Integration:** The Python app sends the prompt to Gemini and
  displays the generated response.
- **Controlled/Structured Output:** The model is instructed to return
  Summary → Key Points → Quiz.
"""
)
st.caption("AI StudyMate • Mini Generative AI Internship Project")
