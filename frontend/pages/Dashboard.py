import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("📊 Recruitment Dashboard")

dashboard = requests.get(
    "http://127.0.0.1:8000/dashboard"
).json()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Jobs",dashboard["total_jobs"])
c2.metric("Companies",dashboard["total_companies"])
c3.metric("Skills",dashboard["total_skills"])
c4.metric("Average Salary",f"${dashboard['average_salary']:,.0f}")

st.divider()

work = requests.get(
    "http://127.0.0.1:8000/charts/work-types"
).json()

df = pd.DataFrame(work)

fig = px.pie(
    df,
    names="work_type",
    values="count",
    title="Work Type Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

salary = requests.get(
    "http://127.0.0.1:8000/charts/salary-distribution"
).json()

fig = px.histogram(
    salary,
    nbins=25,
    title="Salary Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)