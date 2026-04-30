import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(page_title="PhonePe Dashboard", layout="wide")

st.title("📊 PhonePe Transaction Insights Dashboard")

# Load Data from SQL
conn = sqlite3.connect("phonepe.db")
df = pd.read_sql("SELECT * FROM transactions", conn)

# Sidebar
st.sidebar.header("Filters")
state = st.sidebar.selectbox("Select State", df["state"].unique())

filtered_df = df[df["state"] == state]

# Charts
st.subheader("Total Transactions by Category")

category_data = filtered_df.groupby("category")["amount"].sum()

fig, ax = plt.subplots()
category_data.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Top Districts
st.subheader("Top Districts")

district_data = filtered_df.groupby("district")["amount"].sum().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
district_data.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# Raw Data
st.subheader("Raw Data")
st.dataframe(filtered_df)
