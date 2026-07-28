import pandas as pd
import requests
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
amfi_codes = fund_master["amfi_code"]
print("Validating AMFI Codes...\n")

for code in amfi_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        print(f"{code} : Valid")
    else:
        print(f"{code} : Invalid")