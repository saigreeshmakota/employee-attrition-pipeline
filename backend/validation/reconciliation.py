\
import pandas as pd

from sqlalchemy import text
from backend.database.connection import engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

SOURCE_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)

# Read source CSV
source_df = pd.read_csv(SOURCE_FILE)

# Fetch target employee IDs from MySQL
with engine.connect() as connection:
    target_df = pd.read_sql(
        text("SELECT EmployeeNumber FROM employees"),
        connection
    )

# Create sets of employee IDs
source_ids = set(source_df["EmployeeNumber"])
target_ids = set(target_df["EmployeeNumber"])

# Find missing and unexpected IDs
missing_in_target = source_ids - target_ids
unexpected_in_target = target_ids - source_ids

print("\nEMPLOYEE ID RECONCILIATION")
print("--------------------------------")
print("Source unique IDs:", len(source_ids))
print("Target unique IDs:", len(target_ids))
print("Missing IDs in target:", len(missing_in_target))
print("Unexpected IDs in target:", len(unexpected_in_target))

if not missing_in_target and not unexpected_in_target:
    print("Employee ID Reconciliation: PASS")
else:
    print("Employee ID Reconciliation: FAIL")
