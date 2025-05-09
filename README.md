# Personal Finance Tracker

This is a personal finance tracking project built with **Python**, using **Streamlit** for the interactive interface and **SQLite** as the local database. The application allows recording of income and expenses, and viewing a dashboard with monthly summaries and charts.

## Features

- Input form to register income or expense entries  
- Interactive dashboard with visualizations  
- Support for dates and custom categories  
- Local storage using SQLite (cloud-ready in the future)  
- Modular code structure following best practices  

## Technologies Used

- Python 3.10+  
- Streamlit  
- SQLite  
- Plotly  
- Pandas  

## Folder Structure

```bash
.
├── main.py               # Main page
├── pages/
│   ├── dashboard.py     # Dashboard and visualizations
│   └── input_form.py    # Input form
├── database/
│   └── db.py            # SQLite connection
├── .gitignore
├── requirements.txt
└── README.md

```


## How to Run Locally
- Clone the repo.
- git clone https://github.com/lucasfazzib/personal_finance_tracker.git
- cd personal_finance_tracker

## Create and activate a virtual environment:
- python -m venv .venv
- source .venv/Scripts/activate

## Install dependencies:
- pip install -r requirements.txt

## Run the application:
- streamlit run main.py


##  Next Steps

- Financial goal calculations
- Export data to Excel/CSV
- Add basic login for multi-user support
- Login system with token-based authentication (JWT, OAuth2)
- Export monthly financial reports as PDF
- Spending alerts by category or limit threshold
- Recurring transactions with automated scheduling
- Calendar view for monthly income and expense tracking
- Insights and recommendations based on spending habits
- Deploy on Streamlit Cloud, Render, or Azure App Services
- Plugin to import bank or credit card statements (CSV/OFX format)

## Motivation
This project was born out of the need for a more visual and dynamic way to manage personal finances. It also serves as a real-world learning project and portfolio piece, with the potential to evolve into a more robust application. Still under active development.