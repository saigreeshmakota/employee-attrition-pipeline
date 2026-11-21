
USE employee_attrition_db;

-- RECON001: Check duplicate IDs in target
SELECT EmployeeNumber, COUNT(*) AS duplicate_count
FROM employees
GROUP BY EmployeeNumber
HAVING COUNT(*) > 1;

-- RECON002: Check target employee ID range
SELECT
    MIN(EmployeeNumber) AS minimum_employee_id,
    MAX(EmployeeNumber) AS maximum_employee_id,
    COUNT(DISTINCT EmployeeNumber) AS unique_employee_ids
FROM employees;
