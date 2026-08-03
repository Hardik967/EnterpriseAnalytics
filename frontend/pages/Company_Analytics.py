import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("🏢 Company Analytics")

companies = requests.get(
    "http://127.0.0.1:8000/companies/top-hiring"
).json()

df = pd.DataFrame(companies)

fig = px.bar(
    df,
    x="company",
    y="jobs",
    title="Top Hiring Companies"
)

st.plotly_chart(fig, use_container_width=True)