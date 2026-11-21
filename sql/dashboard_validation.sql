
USE employee_attrition_db;

-- TEST 1: Total employee count
SELECT
    'DASH001 - Total Employees' AS test_case,
    COUNT(DISTINCT EmployeeNumber) AS actual_result
FROM employees;


-- TEST 2: Employees who left
SELECT
    'DASH002 - Employees Left' AS test_case,
    COUNT(DISTINCT EmployeeNumber) AS actual_result
FROM employees
WHERE Attrition = 'Yes';


-- TEST 3: Attrition percentage
SELECT
    'DASH003 - Attrition Rate' AS test_case,
    ROUND(
        COUNT(DISTINCT CASE
            WHEN Attrition = 'Yes' THEN EmployeeNumber
        END) * 100.0
        / COUNT(DISTINCT EmployeeNumber),
        2
    ) AS actual_result
FROM employees;


-- TEST 4: Average monthly income
SELECT
    'DASH004 - Average Monthly Income' AS test_case,
    ROUND(AVG(MonthlyIncome), 2) AS actual_result
FROM employees;

-- TEST 5: Department-wise attrition validation

SELECT
    Department,
    COUNT(DISTINCT EmployeeNumber) AS total_employees,
    COUNT(DISTINCT CASE
        WHEN Attrition = 'Yes' THEN EmployeeNumber
    END) AS employees_left,
    ROUND(
        COUNT(DISTINCT CASE
            WHEN Attrition = 'Yes' THEN EmployeeNumber
        END) * 100.0
        / COUNT(DISTINCT EmployeeNumber),
        2
    ) AS attrition_rate
FROM employees
GROUP BY Department
ORDER BY Department;
-- TEST 6: Gender-wise attrition validation

SELECT
    Gender,
    COUNT(DISTINCT EmployeeNumber) AS total_employees,
    COUNT(DISTINCT CASE
        WHEN Attrition = 'Yes' THEN EmployeeNumber
    END) AS employees_left,
    ROUND(
        COUNT(DISTINCT CASE
            WHEN Attrition = 'Yes' THEN EmployeeNumber
        END) * 100.0
        / COUNT(DISTINCT EmployeeNumber),
        2
    ) AS attrition_rate
FROM employees
GROUP BY Gender
ORDER BY Gender;
