import pandas as pd
import os
from sqlalchemy import create_engine
RAW_FOLDER = "data/raw/"
PROCESSED_FOLDER = "data/processed/"
DATABASE_FOLDER = "database/"
DATABASE_NAME = "bluestock_mf.db"
os.makedirs(DATABASE_FOLDER, exist_ok=True)
engine = create_engine(
    f"sqlite:///{DATABASE_FOLDER}{DATABASE_NAME}"
)
processed_files = os.listdir(PROCESSED_FOLDER)
print("Processed Files Found:")
print(processed_files)

print("\nLoading datasets into SQLite...\n")

for file in processed_files:

    if file.endswith(".csv"):

        df = pd.read_csv(PROCESSED_FOLDER + file)

        table_name = file.replace(".csv", "")

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded table: {table_name} ({len(df)} rows)")

print("\nAll datasets loaded successfully!")
