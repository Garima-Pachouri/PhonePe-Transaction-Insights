-- Total Transactions by State
SELECT state, SUM(amount) as total_amount
FROM transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Top 10 Districts
SELECT district, SUM(amount) as total_amount
FROM transactions
GROUP BY district
ORDER BY total_amount DESC
LIMIT 10;

-- Payment Category Distribution
SELECT category, COUNT(*) as count
FROM transactions
GROUP BY category;

-- User Engagement
SELECT state, COUNT(user_id) as users
FROM transactions
GROUP BY state;

-- Insurance Analysis
SELECT insurance_type, SUM(amount)
FROM transactions
GROUP BY insurance_type;
