# Dashboard Testing Report

## 1. KPI Validation

| Test ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| DASH001 | Validate total employees | 1470 | 1470 | PASS |
| DASH002 | Validate employees left | 237 | 237 | PASS |
| DASH003 | Validate attrition rate | 16.12% | 16.12% | PASS |
| DASH004 | Validate average monthly income | 6502.93 | 6502.93 | PASS |

## 2. Department-wise Attrition Validation

| Department | Total Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| Human Resources | 63 | 12 | 19.05% |
| Research & Development | 961 | 133 | 13.84% |
| Sales | 446 | 92 | 20.63% |

Status: PASS

## 3. Overall Result

KPI validation: 4/4 PASS
Department aggregation: PASS

Source: MySQL employee_attrition_db
Dashboard: Streamlit

## 4. Dashboard Functional Testing

| Test ID | Test Scenario | Expected Behaviour | Actual Behaviour | Status |
|---|---|---|---|---|
| DASH007 | Department filter – Sales | Display only Sales employees | Values updated correctly | PASS |
| DASH008 | Gender filter – Female/Male | Display selected gender records | Values updated correctly | PASS |
| DASH009 | Attrition filter – Yes/No | Display selected attrition records | Values updated correctly | PASS |
| DASH010 | Combined filters | Apply all selected filters together | Dashboard updated correctly | PASS |

## 5. Dashboard QA Summary

- KPI validation: 4/4 passed
- Department-wise SQL validation: Passed
- Gender-wise SQL validation: Passed
- Department filter: Passed
- Gender filter: Passed
- Attrition filter: Passed
- Combined filter: Passed

Overall: All executed dashboard tests passed.

Note: Empty-result handling and visual chart verification are still pending.