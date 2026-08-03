import streamlit as st
import requests

st.title("🤖 AI Recruitment Assistant")

question = st.text_area(
    "Ask anything about recruitment, jobs or skills"
)

if st.button("Ask AI"):

    if question:

        with st.spinner("Thinking..."):

            response = requests.post(
                "http://127.0.0.1:8000/ai/insights",
                json={
                    "question": question
                }
            )

            answer = response.json()["answer"]

            st.success(answer)