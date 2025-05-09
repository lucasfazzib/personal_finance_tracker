import streamlit as st

st.set_page_config(page_title="Finance Tracker", layout="wide")

st.title("📊 Personal Finance Dashboard")

st.markdown("""
Welcome to your personal finance control system! 👋

Use the menu on the left to:
- Insert income or expense entries
- View dashboard with charts and summaries

All data is securely stored in a local SQLite database (or cloud-ready in the future).
""")


