import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime

# Load data from SQLite
def load_data():
    conn = sqlite3.connect("data/finances.db")
    df = pd.read_sql("SELECT * FROM transactions", conn, parse_dates=['date'])
    conn.close()
    return df

st.title("Financial Dashboard")

# Load and filter data
df = load_data()

if df.empty:
    st.warning("No financial records found.")
    st.stop()

# Filters
st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", value=df['date'].min().date())
end_date = st.sidebar.date_input("End Date", value=df['date'].max().date())
category_filter = st.sidebar.multiselect("Category", options=df['category'].unique(), default=df['category'].unique())

filtered_df = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date)) & (df['category'].isin(category_filter))]

# Summary cards
st.subheader("Summary")
col1, col2 = st.columns(2)

with col1:
    total_income = filtered_df[filtered_df['type'] == 'Receita']['amount'].sum()
    st.metric("Total Income", f"R$ {total_income:,.2f}")

with col2:
    total_expense = filtered_df[filtered_df['type'] == 'Despesa']['amount'].sum()
    st.metric("Total Expense", f"R$ {total_expense:,.2f}")

# Chart: Monthly trend
st.subheader("Monthly Trends")
monthly = filtered_df.copy()
monthly['month'] = monthly['date'].dt.to_period('M').astype(str)
monthly_grouped = monthly.groupby(['month', 'type'])['amount'].sum().reset_index()
fig = px.bar(monthly_grouped, x='month', y='amount', color='type', barmode='group', title="Monthly Income vs Expense")
st.plotly_chart(fig, use_container_width=True)

# Table view
st.subheader("Detailed Transactions")
st.dataframe(filtered_df.sort_values(by="date", ascending=False), use_container_width=True)
