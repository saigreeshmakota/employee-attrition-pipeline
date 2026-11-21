
import pandas as pd
from pathlib import Path
from sqlalchemy import text
from backend.database.connection import engine

# Project directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Source dataset
SOURCE_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)

# Load source CSV
source_df = pd.read_csv(SOURCE_FILE)

# Load target MySQL records
with engine.connect() as connection:
    target_df = pd.read_sql(
        text("SELECT * FROM employees"),
        connection
    )

# Sort records by employee ID
source_df = source_df.sort_values(
    "EmployeeNumber"
).reset_index(drop=True)

target_df = target_df.sort_values(
    "EmployeeNumber"
).reset_index(drop=True)

# Check column availability
source_columns = set(source_df.columns)
target_columns = set(target_df.columns)

if source_columns != target_columns:
    print("FAIL: Source and target columns do not match.")
    print("Missing in target:", source_columns - target_columns)
    print("Extra in target:", target_columns - source_columns)
    raise SystemExit(1)

# Align column order
target_df = target_df[source_df.columns]

# Compare values
comparison = source_df.compare(
    target_df,
    keep_equal=False
)

print("\nCOLUMN-LEVEL RECONCILIATION")
print("--------------------------------")
print("Source records:", len(source_df))
print("Target records:", len(target_df))
print("Columns compared:", len(source_columns))

if comparison.empty:
    print("Mismatched values:", 0)
    print("Column Reconciliation: PASS")
else:
    print("Mismatched values:", len(comparison))
    print("Column Reconciliation: FAIL")
    print("\nMismatch details:")
    print(comparison.head(20))
