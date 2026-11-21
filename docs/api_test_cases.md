# API Testing Test Cases

**Project:** Employee Attrition Analytics – End-to-End Data Quality & Testing Framework

## 1. Test Execution Summary

| Metric | Result |
|---|---:|
| Total Test Cases | 7 |
| Passed | 7 |
| Failed | 0 |
| Skipped | 0 |
| Overall Status | PASS |

## 2. API Test Cases

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| API001 | Verify home endpoint | HTTP 200 and success message | PASS |
| API002 | Retrieve employee records | HTTP 200 and 100 employee records | PASS |
| API003 | Simulate database connection failure | HTTP 500 with appropriate error message | PASS |
| API004 | Validate employee data quality | Employee IDs, income and attrition values are valid | PASS |
| API005 | Verify API record limit | API returns no more than 100 records | PASS |
| API006 | Compare API employee IDs with MySQL | Employee IDs match database records | PASS |
| API007 | Compare API employee fields with MySQL | Selected field values match database records | PASS |

## 3. Test Execution Evidence

**HTML Test Report:** `reports/api_test_report.html`

**Execution Command:**

```bash
python -m pytest tests/test_api.py -v --html=reports/api_test_report.html --self-contained-html