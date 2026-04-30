import pandas as pd
import sqlite3
import os

# Step 1: Load Data
def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Data Loaded Successfully")
    return df

# Step 2: Clean Data
def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    print("Data Cleaned")
    return df

# Step 3: Transform Data
def transform_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    print("Data Transformed")
    return df

# Step 4: Load to SQL
def load_to_sql(df, table_name):
    conn = sqlite3.connect("phonepe.db")
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"{table_name} loaded into database")

# Pipeline Runner
def run_pipeline():
    file_path = "data/phonepe_data.csv"  # change path if needed
    
    df = load_data(file_path)
    df = clean_data(df)
    df = transform_data(df)
    
    load_to_sql(df, "transactions")

if __name__ == "__main__":
    run_pipeline()
