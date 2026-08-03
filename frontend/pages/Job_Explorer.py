import streamlit as st
import pandas as pd
import requests

st.title("💼 Job Explorer")

jobs = requests.get(
    "http://127.0.0.1:8000/jobs"
).json()

df = pd.DataFrame(jobs)

search = st.text_input("Search Job")

if search:
    df = df[df["title"].str.contains(search, case=False, na=False)]

st.dataframe(df, use_container_width=True)