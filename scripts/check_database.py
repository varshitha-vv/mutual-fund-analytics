import sqlite3
import pandas as pd
import os

DATABASE = "database/bluestock_mf.db"
PROCESSED = "data/processed/"

# Connect to SQLite
conn = sqlite3.connect(DATABASE)

# Get all table names
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Tables in Database:")
print(tables)

print("\n" + "="*60)
print("ROW COUNT VERIFICATION")
print("="*60)

for file in os.listdir(PROCESSED):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        csv_df = pd.read_csv(PROCESSED + file)

        db_count = pd.read_sql_query(
            f"SELECT COUNT(*) AS rows FROM '{table_name}'",
            conn
        )

        print(f"\nTable : {table_name}")
        print(f"CSV Rows : {len(csv_df)}")
        print(f"DB Rows  : {db_count.iloc[0,0]}")

conn.close()

print("\nVerification Complete!")