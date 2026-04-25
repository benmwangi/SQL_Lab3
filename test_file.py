# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT firstName,jobTitle
FROM employees
JOIN offices
USING(officeCode)
WHERE city='Boston';
""",conn)

# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql("""
SELECT o.officeCode,
COUNT(e.employeeNumber) AS num_employees
FROM offices AS o
LEFT JOIN employees AS e
USING(officeCode)
GROUP BY officeCode
HAVING num_employees = 0;

""",conn)

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT e.firstName,
e.lastName,
o.city,
o.state
FROM employees AS e
LEFT JOIN offices AS o
USING(officeCode)
ORDER BY firstName,lastName;
""",conn)

# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT
contactFirstName,
contactLastName,
phone,
salesRepEmployeeNumber
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber
FROM orders
)
ORDER BY contactLastName;

""",conn)

# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql("""
SELECT
contactFirstName,
contactLastName,
amount,
paymentDate
FROM customers
JOIN payments
USING(customerNumber)
ORDER BY CAST(amount AS REAL) DESC;

""",conn)

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql("""
SELECT
employeeNumber,
firstName,
lastName,
COUNT(customerNumber) AS numCustomers
FROM employees AS e
JOIN customers As c
ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY employeeNumber
HAVING AVG(creditLimit) > 90000
ORDER BY numCustomers DESC
;
""",conn)

# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT
productName,
COUNT(quantityOrdered) AS numorders,
SUM(quantityOrdered) AS totalunits
FROM products
JOIN orderdetails
USING(productCode)
GROUP BY productCode
ORDER BY totalunits DESC
;
""",conn)

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql("""
SELECT productName,
productCode,
COUNT(DISTINCT customerNumber) AS numpurchasers
FROM products
JOIN orderdetails
USING(productCode)
JOIN orders
USING(orderNumber)
GROUP BY productName
ORDER BY numPurchasers DESC;
""",conn)

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
SELECT officeCode,
offices.city,
COUNT(DISTINCT customerNumber) AS n_customers
FROM employees AS e
JOIN customers AS c
ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN offices
USING(officeCode)
GROUP BY officeCode;
""",conn)

# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql("""
SELECT  employeeNumber,
firstName,
lastName,
o.city,
officeCode
FROM employees AS e
JOIN offices AS o
USING(officeCode)
JOIN customers AS c
ON e.employeeNumber = c.salesRepEmployeeNumber
WHERE EXISTS (
    SELECT productName,
    COUNT(DISTINCT customerNumber) AS numPurchasers
    FROM products
    JOIN orderdetails
    USING(productCode)
    JOIN orders
    USING(orderNumber)
    GROUP BY productName
    HAVING numPurchasers < 20
)
GROUP BY employeeNumber
ORDER BY lastName;
""",conn)

# Run this cell without changes

conn.close()