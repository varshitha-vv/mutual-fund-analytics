import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("First 5 Rows")
print(fund_master.head())

print("\nShape")
print(fund_master.shape)

print("\nColumn Names")
print(fund_master.columns)

print("\nData Types")
print(fund_master.dtypes)

print("\nMissing Values")
print(fund_master.isnull().sum())
print("\n" + "=" * 60)
print("BUSINESS EXPLORATION")
print("=" * 60)

print("\nNumber of Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategory Distribution:")
print(fund_master["category"].value_counts())

print("\nRisk Category Distribution:")
print(fund_master["risk_category"].value_counts())

print("\nPlan Distribution:")
print(fund_master["plan"].value_counts())

print("\nAverage Expense Ratio:")
print(fund_master["expense_ratio_pct"].mean())

print("\nAverage Minimum SIP Amount:")
print(fund_master["min_sip_amount"].mean())