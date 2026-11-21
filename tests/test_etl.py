
import pandas as pd
from pathlib import Path

# Locate project directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Source dataset
SOURCE_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "clean_employee_attrition.csv"
)

# Target dataset
TARGET_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)

source_df = pd.read_csv(SOURCE_FILE)
target_df = pd.read_csv(TARGET_FILE)


def test_source_and_target_record_count():
    assert len(source_df) == len(target_df)


def test_transformed_dataset_has_new_columns():
    assert "TenureGroup" in target_df.columns
    assert "ExperienceGroup" in target_df.columns


def test_transformation_does_not_remove_employee_records():
    assert target_df["EmployeeNumber"].is_unique
    assert set(source_df["EmployeeNumber"]) == set(
        target_df["EmployeeNumber"]
    )


def test_categorical_values_are_standardized():
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
        values = target_df[column].dropna().astype(str)
        assert values.eq(values.str.strip()).all()


def test_tenure_groups_are_correct():
    expected_groups = pd.cut(
        source_df["YearsAtCompany"],
        bins=[-1, 1, 5, 10, float("inf")],
        labels=["0-1 years", "2-5 years", "6-10 years", "11+ years"]
    )

    actual_groups = target_df["TenureGroup"].astype("string")

    assert actual_groups.reset_index(drop=True).equals(
        expected_groups.astype("string").reset_index(drop=True)
    )


def test_experience_groups_are_correct():
    expected_groups = pd.cut(
        source_df["TotalWorkingYears"],
        bins=[-1, 2, 5, 10, float("inf")],
        labels=["0-2 years", "3-5 years", "6-10 years", "11+ years"]
    )

    actual_groups = target_df["ExperienceGroup"].astype("string")

    assert actual_groups.reset_index(drop=True).equals(
        expected_groups.astype("string").reset_index(drop=True)
    )
