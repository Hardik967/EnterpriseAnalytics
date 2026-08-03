import streamlit as st
import requests

st.set_page_config(page_title="AI Insights", layout="wide")

st.title("🤖 AI Recruitment Assistant")

st.write("Ask anything about jobs, skills, salaries or recruitment trends.")

question = st.text_area(
    "Enter your question",
    placeholder="Example: What are the top skills for Data Scientists?"
)

if st.button("🚀 Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ai/insights",
                    json={
                        "question": question
                    }
                )

                if response.status_code == 200:

                    answer = response.json()["answer"]

                    st.success("Answer")

                    st.write(answer)

                else:

                    st.error("Backend Error")

                    st.write(response.text)

            except Exception as e:

                st.error(f"Connection Error\n\n{e}")