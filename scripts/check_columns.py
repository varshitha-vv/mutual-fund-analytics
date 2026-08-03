import pandas as pd
import os

PROCESSED = "data/processed/"

for file in sorted(os.listdir(PROCESSED)):

    if file.endswith(".csv"):

        df = pd.read_csv(PROCESSED + file)

        print("\n" + "="*70)
        print(file)
        print("="*70)

        print(df.columns.tolist())