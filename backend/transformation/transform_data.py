
from pathlib import Path
import pandas as pd

# STEP 1: Define project paths

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "clean_employee_attrition.csv"
)

OUTPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)


# STEP 2: Load cleaned dataset

print("Starting data transformation...")

df = pd.read_csv(INPUT_FILE)

original_shape = df.shape

print("Original dataset shape:", original_shape)


# STEP 3: Standardize categorical columns

print("\nStandardizing categorical columns...")

categorical_columns = [
    "Attrition",
    "BusinessTravel",
    "Department",
    "EducationField",
    "Gender",
    "JobRole",
    "MaritalStatus",
    "OverTime"
]

for column in categorical_columns:

    df[column] = df[column].astype("string").str.strip()

print("Categorical columns standardized successfully.")


# STEP 4: Create employee tenure groups

print("\nCreating employee tenure groups...")

df["TenureGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 1, 5, 10, float("inf")],
    labels=["0-1 years", "2-5 years", "6-10 years", "11+ years"]
)

print("Tenure groups created successfully.")


# STEP 5: Create total experience groups

print("\nCreating experience groups...")

df["ExperienceGroup"] = pd.cut(
    df["TotalWorkingYears"],
    bins=[-1, 2, 5, 10, float("inf")],
    labels=["0-2 years", "3-5 years", "6-10 years", "11+ years"]
)

print("Experience groups created successfully.")


# STEP 6: Save transformed dataset

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(OUTPUT_FILE, index=False)


# STEP 7: Display transformation summary

print("\n========== TRANSFORMATION SUMMARY ==========")

print("Original shape:", original_shape)
print("Final shape:", df.shape)

print("\nNew columns created:")
print(["TenureGroup", "ExperienceGroup"])

print("\nTenure group distribution:")
print(df["TenureGroup"].value_counts(sort=False))

print("\nExperience group distribution:")
print(df["ExperienceGroup"].value_counts(sort=False))

print("\nTransformed dataset saved at:")
print(OUTPUT_FILE)

print("\nData transformation completed successfully!")
