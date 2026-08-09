import streamlit as st
import pandas as pd
from rapidfuzz import process

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="College Intelligent Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

data = pd.read_csv("data.csv")

# Make sure question and answer columns are strings
data["QUESTIONS"] = data["QUESTIONS"].astype(str)
data["ANSWERS"] = data["ANSWERS"].astype(str)

questions = (
    data["QUESTIONS"]
    .str.strip()
    .str.lower()
    .tolist()
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🎓 College Intelligent Chatbot")

st.write(
    "Ask a question about the college and I will find the most relevant answer from the dataset."
)

# ---------------------------------------------------------
# CHATBOT INPUT
# ---------------------------------------------------------

user = st.text_input(
    "Ask your question:",
    placeholder="Type your question here..."
)

# ---------------------------------------------------------
# ASK BUTTON
# ---------------------------------------------------------

if st.button("Ask", type="primary"):

    if user.strip() == "":
        st.warning("Please enter a question.")

    else:

        user_clean = user.strip().lower()

        # Find closest matching question
        match = process.extractOne(
            user_clean,
            questions
        )

        # -------------------------------------------------
        # MATCH FOUND
        # -------------------------------------------------

        if match and match[1] >= 60:

            matched_question = match[0]

            # Find answer corresponding to matched question
            answer = data.loc[
                data["QUESTIONS"].astype(str).str.strip().str.lower()
                == matched_question,
                "ANSWERS"
            ].values

            if len(answer) > 0:

                st.success(answer[0])

                # Show matching question
                st.caption(
                    f"Matched question: {matched_question}"
                )

                # Show similarity score
                st.caption(
                    f"Match confidence: {match[1]:.1f}%"
                )

            else:
                st.error("Sorry, I couldn't find the answer.")

        # -------------------------------------------------
        # NO MATCH
        # -------------------------------------------------

        else:

            st.error(
                "Sorry, I don't know the answer to that question."
            )

            st.info(
                "Please try asking one of the questions listed below."
            )


# ---------------------------------------------------------
# ALL QUESTIONS FROM DATASET
# ---------------------------------------------------------

st.markdown("---")

st.subheader("📚 Questions You Can Ask")

st.write(
    f"There are **{len(data)} questions** available in this chatbot."
)

# ---------------------------------------------------------
# DISPLAY ALL QUESTIONS
# ---------------------------------------------------------

with st.expander("🔽 View all questions"):

    for i, question in enumerate(data["QUESTIONS"], start=1):

        st.markdown(
            f"**{i}. {question}**"
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">

    <h3>😊 College Intelligent Chatbot</h3>

    <p><b>Developed by:</b> Paridhi Gakhar</p>

    <p>Powered by Python, Streamlit, Pandas and RapidFuzz</p>

    </div>
    """,
    unsafe_allow_html=True
)