# PhonePe Transaction Insights

This is an end-to-end Data Engineering and Analytics project using PhonePe Pulse data.

## Objective
To extract PhonePe Pulse JSON data, transform it into structured tables, load it into SQL database, analyze business trends, create 20 visualizations, and build an interactive Streamlit dashboard.

## Tech Stack
Python, Pandas, SQLite, SQL, Matplotlib, Seaborn, Plotly, Streamlit

## Project Workflow
1. Extracted raw JSON data from PhonePe Pulse GitHub repository.
2. Transformed nested JSON files into clean Pandas DataFrames.
3. Loaded 9 structured tables into SQLite database.
4. Performed SQL-based business analysis.
5. Created 20 analytical charts with insights and business impact.
6. Built Streamlit dashboard for interactive analysis.

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
