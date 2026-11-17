
from pathlib import Path
import pandas as pd

# ----------------------------------------
# STEP 1: DEFINE PROJECT PATHS
# ----------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

CLEAN_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "clean_employee_attrition.csv"
)

TRANSFORMED_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)


# ----------------------------------------
# STEP 2: LOAD DATASETS
# ----------------------------------------

print("Starting data validation...")

clean_df = pd.read_csv(CLEAN_FILE)
df = pd.read_csv(TRANSFORMED_FILE)

print("Transformed dataset shape:", df.shape)


# ----------------------------------------
# STEP 3: VALIDATE REQUIRED COLUMNS
# ----------------------------------------

print("\nChecking required columns...")

required_columns = [
    "EmployeeNumber",
    "Age",
    "Attrition",
    "MonthlyIncome",
    "TotalWorkingYears",
    "YearsAtCompany",
    "TenureGroup",
    "ExperienceGroup"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

print("Missing required columns:", missing_columns)


# ----------------------------------------
# STEP 4: VALIDATE RECORD COUNT
# ----------------------------------------

print("\nChecking record count...")

record_count_valid = len(df) == len(clean_df)

print("Record count valid:", record_count_valid)


# ----------------------------------------
# STEP 5: CHECK MISSING VALUES
# ----------------------------------------

print("\nChecking missing values...")

missing_values = df.isnull().sum().sum()

print("Total missing values:", missing_values)


# ----------------------------------------
# STEP 6: CHECK DUPLICATE RECORDS
# ----------------------------------------

print("\nChecking duplicate records...")

duplicate_records = df.duplicated().sum()

print("Duplicate records:", duplicate_records)

duplicate_ids = df["EmployeeNumber"].duplicated().sum()

print("Duplicate employee IDs:", duplicate_ids)


# ----------------------------------------
# STEP 7: VALIDATE BUSINESS RULES
# ----------------------------------------

print("\nChecking business rules...")

invalid_age = (~df["Age"].between(18, 65)).sum()

invalid_income = (df["MonthlyIncome"] < 0).sum()

invalid_experience = (
    (df["YearsAtCompany"] > df["TotalWorkingYears"])
).sum()

invalid_attrition = (
    ~df["Attrition"].isin(["Yes", "No"])
).sum()

invalid_role_years = (
    df["YearsInCurrentRole"] > df["YearsAtCompany"]
).sum()

print("Invalid age records:", invalid_age)
print("Invalid income records:", invalid_income)
print("Invalid experience records:", invalid_experience)
print("Invalid attrition records:", invalid_attrition)
print("Invalid current role experience:", invalid_role_years)


# ----------------------------------------
# STEP 8: VALIDATE NEW FEATURES
# ----------------------------------------

print("\nChecking transformed features...")

missing_tenure_groups = df["TenureGroup"].isnull().sum()

missing_experience_groups = df["ExperienceGroup"].isnull().sum()

print("Missing tenure groups:", missing_tenure_groups)

print("Missing experience groups:", missing_experience_groups)


# ----------------------------------------
# STEP 9: FINAL VALIDATION REPORT
# ----------------------------------------

checks = {
    "Required columns": len(missing_columns) == 0,
    "Record count": record_count_valid,
    "Missing values": missing_values == 0,
    "Duplicate records": duplicate_records == 0,
    "Unique employee IDs": duplicate_ids == 0,
    "Valid age": invalid_age == 0,
    "Valid income": invalid_income == 0,
    "Valid experience": invalid_experience == 0,
    "Valid attrition": invalid_attrition == 0,
    "Valid current role experience": invalid_role_years == 0,
    "Tenure groups": missing_tenure_groups == 0,
    "Experience groups": missing_experience_groups == 0
}

print("\n========== FINAL VALIDATION REPORT ==========")

for check, result in checks.items():

    status = "PASSED" if result else "FAILED"

    print(f"{check}: {status}")


if all(checks.values()):

    print("\nDATA VALIDATION SUCCESSFUL!")

else:

    print("\nDATA VALIDATION FAILED!")
    raise ValueError("One or more data quality checks failed.")
