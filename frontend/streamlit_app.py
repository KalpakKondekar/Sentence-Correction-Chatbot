import streamlit as st
import requests

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000/chat"
)

st.set_page_config(
    page_title="Sentence Corrector Bot",
    page_icon="🤖"
)

st.title("🤖 AI Sentence Corrector")

user_input = st.text_area(
    "Enter your sentence"
)

if st.button("Correct Sentence"):

    if user_input.strip() == "":
        st.warning("Please enter a sentence")
    else:

        response = requests.post(
            BACKEND_URL,
            json={"text": user_input}
        )

        result = response.json()

        st.subheader("Corrected Sentence")

        st.success(result["corrected"])