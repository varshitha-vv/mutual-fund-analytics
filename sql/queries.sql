SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM 03_aum_by_fund_house_cleaned
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM 02_nav_history_cleaned
GROUP BY month
ORDER BY month;
SELECT
    SUM(amount_inr) AS total_sip
FROM 08_investor_transactions_cleaned
WHERE transaction_type='SIP';
SELECT
    state,
    COUNT(*) AS total_transactions
FROM 08_investor_transactions_cleaned
GROUP BY state
ORDER BY total_transactions DESC;
SELECT
    scheme_name,
    expense_ratio_pct
FROM 07_scheme_performance_cleaned
WHERE expense_ratio_pct < 1;
SELECT
    scheme_name,
    return_1yr_pct
FROM 07_scheme_performance_cleaned
ORDER BY return_1yr_pct DESC
LIMIT 5;
SELECT
    fund_house,
    AVG(expense_ratio_pct) AS avg_expense
FROM 07_scheme_performance_cleaned
GROUP BY fund_house;
SELECT
    payment_mode,
    AVG(amount_inr) AS average_amount
FROM 08_investor_transactions_cleaned
GROUP BY payment_mode;
SELECT
    category,
    COUNT(*) AS schemes
FROM 01_fund_master_cleaned
GROUP BY category;
SELECT
    scheme_name,
    morningstar_rating
FROM 07_scheme_performance_cleaned
ORDER BY morningstar_rating DESC
LIMIT 5;