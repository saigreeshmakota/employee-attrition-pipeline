
-- PROJECT: Employee Attrition Analytics Pipeline
-- MODULE: SQL Data Quality Testing
-- DATABASE: employee_attrition_db
-- TABLE: employees

USE employee_attrition_db;

-- SQL001: Total record count
SELECT 'SQL001 - Total Records' AS test_case,
       COUNT(*) AS actual_result
FROM employees;

-- SQL002: Duplicate employee IDs
SELECT 'SQL002 - Duplicate IDs' AS test_case,
       COUNT(*) AS actual_result
FROM (
    SELECT EmployeeNumber
    FROM employees
    GROUP BY EmployeeNumber
    HAVING COUNT(*) > 1
) AS duplicates;

-- SQL003: Missing employee IDs
SELECT 'SQL003 - Missing IDs' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE EmployeeNumber IS NULL;

-- SQL004: Invalid employee ages
SELECT 'SQL004 - Invalid Ages' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE Age IS NULL OR Age < 18 OR Age > 65;

-- SQL005: Invalid monthly income
SELECT 'SQL005 - Invalid Income' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE MonthlyIncome IS NULL OR MonthlyIncome < 0;

-- SQL006: Invalid attrition values
SELECT 'SQL006 - Invalid Attrition' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE Attrition IS NULL
   OR Attrition NOT IN ('Yes', 'No');

-- SQL007: Missing departments
SELECT 'SQL007 - Missing Departments' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE Department IS NULL OR TRIM(Department) = '';

-- SQL008: Missing job roles
SELECT 'SQL008 - Missing Job Roles' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE JobRole IS NULL OR TRIM(JobRole) = '';

-- SQL009: Invalid years at company
SELECT 'SQL009 - Invalid Company Years' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE YearsAtCompany IS NULL OR YearsAtCompany < 0;

-- SQL010: Invalid total working years
SELECT 'SQL010 - Invalid Working Years' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE TotalWorkingYears IS NULL OR TotalWorkingYears < 0;

-- SQL011: Missing tenure groups
SELECT 'SQL011 - Missing Tenure Groups' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE TenureGroup IS NULL;

-- SQL012: Missing experience groups
SELECT 'SQL012 - Missing Experience Groups' AS test_case,
       COUNT(*) AS actual_result
FROM employees
WHERE ExperienceGroup IS NULL;
