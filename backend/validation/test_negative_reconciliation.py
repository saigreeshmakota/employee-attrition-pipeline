
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

SOURCE_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)

# Load a temporary copy of source data
source_df = pd.read_csv(SOURCE_FILE)

# Create a separate test copy
target_test_df = source_df.copy()

# Introduce a controlled mismatch
employee_id = target_test_df["EmployeeNumber"].iloc[0]

target_test_df.loc[
    target_test_df["EmployeeNumber"] == employee_id,
    "MonthlyIncome"
] += 500

# Compare source and temporary target
comparison = source_df.compare(
    target_test_df,
    keep_equal=False
)

print("\nNEGATIVE RECONCILIATION TEST")
print("--------------------------------")
print("Test employee ID:", employee_id)
print("Test column: MonthlyIncome")
print("Expected mismatches: 1")
print("Actual mismatches:", len(comparison))

if len(comparison) == 1:
    print("Negative Test: PASS")
    print("The incorrect value was successfully detected.")
else:
    print("Negative Test: FAIL")
