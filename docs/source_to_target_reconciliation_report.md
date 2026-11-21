
# Source-to-Target Reconciliation Test Report

## 1. Project Information

- **Project:** Employee Attrition Analytics Pipeline
- **Testing Area:** Data Quality and ETL Testing
- **Test Type:** Source-to-Target Reconciliation
- **Source:** Transformed Employee Attrition CSV
- **Target:** MySQL `employee_attrition_db.employees`

## 2. Test Execution Summary

| Test ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| RECON001 | Compare source and target record counts | Both should contain 1470 records | Source: 1470, Target: 1470 | PASS |
| RECON002 | Compare EmployeeNumber values | No missing or unexpected IDs | Missing: 0, Unexpected: 0 | PASS |
| RECON003 | Compare source and target columns and values | No data mismatches | 34 columns compared, 0 mismatched values reported | PASS |
| NEG001 | Introduce an incorrect MonthlyIncome value in a temporary copy | Reconciliation should detect the mismatch | 1 mismatched row detected | PASS |

## 3. Detailed Test Results

### RECON001 – Record Count Validation

**Objective:** Verify that all source records have been loaded into the target database.

- Source record count: 1470
- Target record count: 1470
- Expected: Both counts must match.
- Result: PASS

### RECON002 – Employee ID Validation

**Objective:** Verify that all employee IDs in the source are available in the target.

- Source unique IDs: 1470
- Target unique IDs: 1470
- Missing IDs: 0
- Unexpected IDs: 0
- Result: PASS

### RECON003 – Column-Level Reconciliation

**Objective:** Compare source and target data across all columns.

- Source records: 1470
- Target records: 1470
- Columns compared: 34
- Mismatched values reported: 0
- Result: PASS

### NEG001 – Negative Reconciliation Testing

**Objective:** Verify that the reconciliation process detects incorrect data.

**Test procedure:**
1. Created a temporary copy of the source dataset.
2. Selected EmployeeNumber 1.
3. Increased MonthlyIncome by 500 in the temporary copy.
4. Compared the original and modified datasets.

**Expected:** The incorrect value should be detected.

**Actual:** One mismatched row was detected.

**Result:** PASS

Note: This test used a temporary DataFrame and did not modify the actual CSV or MySQL database.

## 4. Overall Conclusion

All four executed reconciliation test scenarios passed.

The testing demonstrated:
- Source-to-target record count validation.
- Employee ID completeness validation.
- Column-level data comparison.
- Detection of intentionally introduced incorrect data.

The results provide evidence that the current source and target datasets are consistent and that the negative test can detect a controlled data mismatch.
