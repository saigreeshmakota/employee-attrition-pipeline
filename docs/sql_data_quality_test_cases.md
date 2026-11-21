
# SQL Data Quality Testing Report

## 1. Project Information

Project: Employee Attrition Analytics and Prediction Pipeline

Module: SQL Data Quality Testing

Database: employee_attrition_db

Table: employees

Source Dataset: transformed_employee_attrition.csv

Expected Record Count: 1470

Actual Record Count: 1470

Total Columns: 34

## 2. Testing Objective

To validate the completeness, uniqueness, validity and
consistency of employee records stored in MySQL after ETL loading.

## 3. Test Execution Summary

| Metric | Result |
|---|---:|
| Total Test Cases | 12 |
| Passed | 12 |
| Failed | 0 |
| Blocked | 0 |
| Pass Percentage | 100% |

## 4. Detailed Test Results

| Test ID | Column | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| SQL001 | All records | 1470 | 1470 | PASS |
| SQL002 | EmployeeNumber | 0 duplicates | 0 | PASS |
| SQL003 | EmployeeNumber | 0 NULLs | 0 | PASS |
| SQL004 | Age | 0 invalid | 0 | PASS |
| SQL005 | MonthlyIncome | 0 invalid | 0 | PASS |
| SQL006 | Attrition | 0 invalid | 0 | PASS |
| SQL007 | Department | 0 missing | 0 | PASS |
| SQL008 | JobRole | 0 missing | 0 | PASS |
| SQL009 | YearsAtCompany | 0 invalid | 0 | PASS |
| SQL010 | TotalWorkingYears | 0 invalid | 0 | PASS |
| SQL011 | TenureGroup | 0 missing | 0 | PASS |
| SQL012 | ExperienceGroup | 0 missing | 0 | PASS |

## 5. Test Execution Evidence

Execution output:
reports/sql_validation_output.txt

SQL scripts:
sql/validation_queries.sql

## 6. Conclusion

All 12 executed SQL data-quality validation checks
returned their expected results.

No violations were detected by these checks in the
1470 employee records loaded into MySQL.

## 7. Limitations

These checks cover selected data-quality rules.
They do not establish complete accuracy of every
column or source-to-target value reconciliation.
