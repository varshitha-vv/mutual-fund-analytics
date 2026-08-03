import pandas as pd
import os

RAW_FOLDER = "data/raw/"
PROCESSED_FOLDER = "data/processed/"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

nav_df = pd.read_csv(RAW_FOLDER + "02_nav_history.csv")

print("First 5 Rows")
print(nav_df.head())

print("\nShape")
print(nav_df.shape)

print("\nData Types")
print(nav_df.dtypes)

print("\nMissing Values")
print(nav_df.isnull().sum())
print("\nConverting date column to datetime...")

nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    dayfirst=True,
    errors="coerce"
)

print("Updated Data Types")
print(nav_df.dtypes)
print("\nSorting data by AMFI Code and Date...")

nav_df = nav_df.sort_values(
    by=["amfi_code", "date"]
)

print(nav_df.head())
print("\nMissing NAV values before forward fill:")
print(nav_df["nav"].isnull().sum())

nav_df["nav"] = (
    nav_df.groupby("amfi_code")["nav"]
    .ffill()
)

print("\nMissing NAV values after forward fill:")
print(nav_df["nav"].isnull().sum())
print("\nNumber of rows before removing duplicates:")
print(nav_df.shape[0])

nav_df = nav_df.drop_duplicates()

print("\nNumber of rows after removing duplicates:")
print(nav_df.shape[0])
print("\nChecking for invalid NAV values...")

invalid_nav = nav_df[nav_df["nav"] <= 0]

print("Invalid NAV Records:")
print(invalid_nav)

nav_df = nav_df[nav_df["nav"] > 0]

print("\nRemaining Rows:")
print(nav_df.shape[0])
output_file = PROCESSED_FOLDER + "02_nav_history_cleaned.csv"

nav_df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print(f"Saved to: {output_file}")
# ==========================================
# CLEAN INVESTOR TRANSACTIONS
# ==========================================

print("\n" + "="*60)
print("CLEANING INVESTOR TRANSACTIONS")
print("="*60)

txn_df = pd.read_csv(RAW_FOLDER + "08_investor_transactions.csv")

print("\nFirst 5 Rows")
print(txn_df.head())

print("\nShape")
print(txn_df.shape)

print("\nColumn Names")
print(txn_df.columns)

print("\nData Types")
print(txn_df.dtypes)

print("\nMissing Values")
print(txn_df.isnull().sum())
print("\nUnique Transaction Types:")
print(txn_df["transaction_type"].unique())
print("\nStandardizing Transaction Types...")

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

txn_df["transaction_type"] = txn_df["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

print("Updated Transaction Types:")
print(txn_df["transaction_type"].unique())
print("\nChecking Invalid Transaction Amounts...")

invalid_amount = txn_df[txn_df["amount_inr"] <= 0]

print("Number of Invalid Records:")
print(len(invalid_amount))

txn_df = txn_df[txn_df["amount_inr"] > 0]

print("Remaining Records:")
print(len(txn_df))
print("\nConverting Transaction Date...")

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"],
    errors="coerce"
)

print(txn_df.dtypes)
print("\nUnique KYC Status Values:")
print(txn_df["kyc_status"].unique())

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = txn_df[
    ~txn_df["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Records:")
print(len(invalid_kyc))
print("\nRemoving Duplicate Records...")

print("Before:", len(txn_df))

txn_df = txn_df.drop_duplicates()

print("After:", len(txn_df))
txn_output = PROCESSED_FOLDER + "08_investor_transactions_cleaned.csv"

txn_df.to_csv(txn_output, index=False)

print("\nInvestor Transactions cleaned successfully!")
print(f"Saved to: {txn_output}")
# ==========================================
# CLEAN SCHEME PERFORMANCE
# ==========================================

print("\n" + "="*60)
print("CLEANING SCHEME PERFORMANCE")
print("="*60)

perf_df = pd.read_csv(RAW_FOLDER + "07_scheme_performance.csv")

print("\nFirst 5 Rows")
print(perf_df.head())

print("\nShape")
print(perf_df.shape)

print("\nColumn Names")
print(perf_df.columns)

print("\nData Types")
print(perf_df.dtypes)

print("\nMissing Values")
print(perf_df.isnull().sum())
print("\nConverting Return Columns to Numeric...")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

print("\nUpdated Data Types")
print(perf_df[return_columns].dtypes)
print("\nChecking Expense Ratio...")

expense_anomalies = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1) |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(expense_anomalies)

print("\nNumber of Anomalies:")
print(len(expense_anomalies))
print("\nChecking Return Value Anomalies...")

return_anomalies = perf_df[
    (perf_df["return_1yr_pct"] < -100) |
    (perf_df["return_1yr_pct"] > 100) |
    (perf_df["return_3yr_pct"] < -100) |
    (perf_df["return_3yr_pct"] > 100) |
    (perf_df["return_5yr_pct"] < -100) |
    (perf_df["return_5yr_pct"] > 100)
]

print(return_anomalies)

print("\nNumber of Return Anomalies:")
print(len(return_anomalies))
print("\nRemoving Duplicate Records...")

print("Before:", len(perf_df))

perf_df = perf_df.drop_duplicates()

print("After:", len(perf_df))
perf_output = PROCESSED_FOLDER + "07_scheme_performance_cleaned.csv"

perf_df.to_csv(
    perf_output,
    index=False
)

print("\nScheme Performance cleaned successfully!")
print(f"Saved to: {perf_output}")
# ==========================================
# CLEAN REMAINING DATASETS
# ==========================================

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("\nCleaning Remaining Datasets...")

for file in remaining_files:

    df = pd.read_csv(RAW_FOLDER + file)

    print(f"\nCleaning {file}...")

    print("Rows before:", len(df))

    df = df.drop_duplicates()

    print("Rows after :", len(df))

    output_name = file.replace(".csv", "_cleaned.csv")

    df.to_csv(PROCESSED_FOLDER + output_name, index=False)

    print(f"Saved: {output_name}")

print("\nAll remaining datasets cleaned successfully!")