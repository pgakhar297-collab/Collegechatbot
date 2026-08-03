import streamlit as st
import pandas as pd
from rapidfuzz import process

# Load data
data = pd.read_csv("data.csv")

st.title("🎓 College Intelligent Chatbot")

user = st.text_input("Ask your question:")

if st.button("Ask"):
    user = user.strip().lower()

    questions = data["QUESTIONS"].astype(str).str.strip().str.lower().tolist()

    match = process.extractOne(user, questions)

    if match and match[1] >= 60:
        matched_question = match[0]
        answer = data.loc[
            data["QUESTIONS"].astype(str).str.strip().str.lower() == matched_question,
            "ANSWERS"
        ].values[0]

        st.success(answer)
    else:
        st.error("Sorry, I don't know the answer.")
