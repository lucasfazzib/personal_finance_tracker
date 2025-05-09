import streamlit as st
import sqlite3
import pandas as pd
from datetime import date
import os

# Ensure the database folder exists
DB_PATH = "data/finances.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Create connection
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        amount REAL NOT NULL,
        recurring TEXT,
        notes TEXT
    )
''')
conn.commit()

st.title("Financial Entry Form")

with st.form("entry_form"):
    col1, col2 = st.columns(2)
    with col1:
        entry_date = st.date_input("Date", value=date.today())
        entry_type = st.selectbox("Type", ["Receita", "Despesa"])
        category = st.text_input("Category")
    with col2:
        amount = st.number_input("Amount (R$)", min_value=0.0, step=0.01)
        recurring = st.selectbox("Recurring?", ["Não", "Sim"])
        description = st.text_input("Description")

    notes = st.text_area("Notes (Optional)")
    submitted = st.form_submit_button("💾 Save Entry")

    if submitted:
        c.execute('''
            INSERT INTO transactions (date, type, category, description, amount, recurring, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (entry_date.isoformat(), entry_type, category, description, amount, recurring, notes))
        conn.commit()
        st.success("✅ Entry saved successfully!")

# Optional: show recent entries
st.subheader("Last Entries")
df = pd.read_sql("SELECT * FROM transactions ORDER BY date DESC LIMIT 5", conn)
st.dataframe(df, use_container_width=True)
