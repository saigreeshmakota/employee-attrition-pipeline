
from pathlib import Path
import pandas as pd

# STEP 1: Define project paths

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"

PROCESSED_FILE = BASE_DIR / "data" / "processed" / "clean_employee_attrition.csv"


# STEP 2: Read raw dataset

print("Starting data cleaning...")

df = pd.read_csv(RAW_FILE)

print("Original dataset shape:", df.shape)


# STEP 3: Check missing values

print("\nChecking missing values...")

print("Total missing values:", df.isnull().sum().sum())


# STEP 4: Remove duplicate records

print("\nChecking duplicate records...")

duplicate_count = df.duplicated().sum()

print("Duplicate records:", duplicate_count)

df = df.drop_duplicates()


# STEP 5: Identify constant columns

print("\nIdentifying constant columns...")

constant_columns = [
    column
    for column in df.columns
    if df[column].nunique(dropna=False) == 1
]

print("Constant columns:", constant_columns)


# STEP 6: Remove constant columns

df = df.drop(columns=constant_columns)

print("Columns removed:", len(constant_columns))


# STEP 7: Save cleaned dataset

PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_FILE, index=False)


# STEP 8: Display final results

print("\n========== CLEANING SUMMARY ==========")

print("Original shape:", (1470, 35))
print("Final shape:", df.shape)
print("Total records:", len(df))
print("Total columns:", len(df.columns))

print("\nCleaned dataset saved at:")
print(PROCESSED_FILE)

print("\nData cleaning completed successfully!")
