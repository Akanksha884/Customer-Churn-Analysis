import pandas as pd
import sqlite3

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

conn = sqlite3.connect("customer_churn.db")

df.to_sql("customer_churn", conn, if_exists="replace", index=False)

print("Done")

query = """
SELECT COUNT(*)
FROM customer_churn
"""

pd.read_sql(query, conn)

query = """
SELECT COUNT(*) AS Churned_Customers
FROM customer_churn
WHERE Churn='Yes';
"""

pd.read_sql(query, conn)

query = """
SELECT COUNT(*) AS Active_Customers
FROM customer_churn
WHERE Churn='No';
"""

pd.read_sql(query, conn)

query = """
SELECT
ROUND(
COUNT(CASE WHEN Churn='Yes' THEN 1 END)*100.0/COUNT(*),2)
AS Churn_Rate
FROM customer_churn;
"""

pd.read_sql(query, conn)

pd.read_sql("""
SELECT
    gender,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY gender;
""", conn)

pd.read_sql("""
SELECT
    SeniorCitizen,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY SeniorCitizen;
""", conn)

pd.read_sql("""
SELECT
    Partner,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY Partner;
""", conn)

pd.read_sql("""
SELECT
    Dependents,
    COUNT(*) AS Total_Customers
FROM customer_churn
GROUP BY Dependents;
""", conn)

pd.read_sql("""
SELECT
ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_churn;
""", conn)

pd.read_sql("""
SELECT
ROUND(AVG(TotalCharges),2) AS Avg_Total_Charges
FROM customer_churn
WHERE TotalCharges!='';
""", conn)

pd.read_sql("""
SELECT
ROUND(AVG(tenure),2) AS Avg_Tenure
FROM customer_churn;
""", conn)

pd.read_sql("""
SELECT
MIN(MonthlyCharges) AS Minimum,
MAX(MonthlyCharges) AS Maximum
FROM customer_churn;
""", conn)

pd.read_sql("""
SELECT
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) / COUNT(*),2) AS Churn_Rate
FROM customer_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;
""", conn)

pd.read_sql("""
SELECT
    InternetService,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY InternetService;
""", conn)

pd.read_sql("""
SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Churned_Customers DESC;
""", conn)

pd.read_sql("""
SELECT
    gender,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY gender;
""", conn)

pd.read_sql("""
SELECT
    SeniorCitizen,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY SeniorCitizen;
""", conn)

pd.read_sql("""
SELECT
    Partner,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY Partner;
""", conn)

pd.read_sql("""
SELECT
    Dependents,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY Dependents;
""", conn)

pd.read_sql("""
SELECT
    PaperlessBilling,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY PaperlessBilling;
""", conn)

pd.read_sql("""
SELECT
    PaperlessBilling,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers
FROM customer_churn
GROUP BY PaperlessBilling;
""", conn)

pd.read_sql("""
SELECT
    Contract,
    ROUND(AVG(CAST(TotalCharges AS REAL)),2) AS Avg_Total_Charges
FROM customer_churn
WHERE TotalCharges != ''
GROUP BY Contract;
""", conn)

pd.read_sql("""
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_churn
GROUP BY Churn;
""", conn)

pd.read_sql("""
SELECT
    Churn,
    ROUND(SUM(CAST(TotalCharges AS REAL)),2) AS Total_Revenue
FROM customer_churn
WHERE TotalCharges != ''
GROUP BY Churn;
""", conn)

pd.read_sql("""
SELECT
    Contract,
    ROUND(AVG(tenure),2) AS Avg_Tenure
FROM customer_churn
GROUP BY Contract;
""", conn)

pd.read_sql("""
SELECT
    InternetService,
    ROUND(SUM(CAST(TotalCharges AS REAL)),2) AS Revenue
FROM customer_churn
WHERE TotalCharges != ''
GROUP BY InternetService;
""", conn)

pd.read_sql("""
SELECT
    customerID,
    MonthlyCharges,
    CASE
        WHEN MonthlyCharges < 35 THEN 'Low'
        WHEN MonthlyCharges BETWEEN 35 AND 70 THEN 'Medium'
        ELSE 'High'
    END AS Customer_Segment
FROM customer_churn
LIMIT 20;
""", conn)

pd.read_sql("""
SELECT
    customerID,
    TotalCharges,
    RANK() OVER (ORDER BY CAST(TotalCharges AS REAL) DESC) AS Revenue_Rank
FROM customer_churn
WHERE TotalCharges != ''
LIMIT 20;
""", conn)

pd.read_sql("""
SELECT
    customerID,
    tenure
FROM customer_churn
ORDER BY tenure DESC
LIMIT 5;
""", conn)

pd.read_sql("""
SELECT
    customerID,
    Contract,
    InternetService,
    MonthlyCharges
FROM customer_churn
WHERE Churn='Yes'
AND Contract='Month-to-month'
AND MonthlyCharges > 70
LIMIT 20;
""", conn)
