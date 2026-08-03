--- ==========================================
-- Dimension Table : Fund
-- ==========================================

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    benchmark TEXT,

    fund_manager TEXT,

    risk_category TEXT,

    launch_date TEXT

);
-- ==========================================
-- Dimension Table : Date
-- ==========================================

CREATE TABLE dim_date (

    date TEXT PRIMARY KEY,

    year INTEGER,

    month INTEGER,

    day INTEGER,

    quarter INTEGER,

    month_name TEXT,

    weekday TEXT

);
-- ==========================================
-- Fact Table : NAV
-- ==========================================

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date TEXT,

    nav REAL,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date) REFERENCES dim_date(date)

);
-- ==========================================
-- Fact Table : Transactions
-- ==========================================

CREATE TABLE fact_transactions (

   transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,

    amfi_code INTEGER,

    transaction_date TEXT,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (transaction_date) REFERENCES dim_date(date)

);
-- ==========================================
-- Fact Table : Performance
-- ==========================================

CREATE TABLE fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date TEXT,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    risk_grade TEXT,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date) REFERENCES dim_date(date)

);
-- ==========================================
-- Fact Table : AUM
-- ==========================================
CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date TEXT,

    aum_crore REAL,

    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date) REFERENCES dim_date(date)

);