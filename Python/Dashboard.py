import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="DS Salary Dashboard", layout="wide")

st.title("📊 Data Science Salary Analytics Dashboard")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('Dataset/Cleaned_Data.csv')

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
work_year = st.sidebar.multiselect("Select Work Year", options=df["work_year"].unique(), default=df["work_year"].unique())
exp_level = st.sidebar.multiselect("Select Experience Level", options=df["experience_level_full"].unique(), default=df["experience_level_full"].unique())

filtered_df = df[(df["work_year"].isin(work_year)) & (df["experience_level_full"].isin(exp_level))]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Roles", len(filtered_df))
col2.metric("Avg Salary", f"${filtered_df['salary_in_usd'].mean():,.0f}")
col3.metric("Max Salary", f"${filtered_df['salary_in_usd'].max():,.0f}")
col4.metric("Remote %", f"{(filtered_df['remote_ratio'] == 100).mean()*100:.1f}%")

# Row 1: Charts
c1, c2 = st.columns(2)

with c1:
    st.subheader("Salary Distribution by Experience Level")
    fig_box = px.box(filtered_df, x="experience_level_full", y="salary_in_usd", color="experience_level_full")
    st.plotly_chart(fig_box, use_container_width=True)

with c2:
    st.subheader("Top 10 Job Titles by Average Salary")
    top_jobs = filtered_df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10).reset_index()
    fig_bar = px.bar(top_jobs, x="salary_in_usd", y="job_title", orientation='h', color="salary_in_usd")
    st.plotly_chart(fig_bar, use_container_width=True)

# Row 2: Trends and Geo
c3, c4 = st.columns(2)

with c3:
    st.subheader("Salary Trend Over Years")
    trend = filtered_df.groupby("work_year")["salary_in_usd"].mean().reset_index()
    fig_line = px.line(trend, x="work_year", y="salary_in_usd", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

with c4:
    st.subheader("Company Location vs Salary")
    loc_salary = filtered_df.groupby("company_location")["salary_in_usd"].mean().reset_index().sort_values("salary_in_usd", ascending=False).head(15)
    fig_geo = px.bar(loc_salary, x="company_location", y="salary_in_usd")
    st.plotly_chart(fig_geo, use_container_width=True)

# Data Table
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)

# Download Button
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download Filtered Data", data=csv, file_name="filtered_ds_salaries.csv", mime="text/csv")
