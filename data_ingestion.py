import os
import pandas as pd
data_folder = "data/raw"
csv_files = [
    file for file in os.listdir(data_folder)
    if file.endswith(".csv")
]
print("CSV Files Found:")
print(csv_files)
dataframes = {}

for file in csv_files:
    file_path = os.path.join(data_folder, file)

    df = pd.read_csv(file_path)

    dataframes[file] = df
    print("\nAll CSV files loaded successfully!")

print("\nLoaded DataFrames:")

for name in dataframes:
    print(name)
    print("\n" + "=" * 60)
print("DATASET EXPLORATION")
print("=" * 60)

for name, df in dataframes.items():

    print(f"\nDataset: {name}")

    print("-" * 40)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n" + "=" * 60)