import pandas as pd 
import pathlib as path 

# locate the project directory 
BASE_DIR = path.Path(__file__).resolve().parents[1]

# lOAD THE Transformed emmployee dataset 

DATA_FILE = BASE_DIR / "data" / "processed" / "transformed_employee_attrition.csv"

df = pd.read_csv(DATA_FILE)

def test_dataset_is_not_empty():
    assert len(df) > 0

def test_required_columns_exist():
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
    for column in required_columns:
        assert column in df.columns
def test_employee_ids_are_unique():
    assert df["EmployeeNumber"].is_unique
def test_no_missing_values():
    assert df.isnull().sum().sum() == 0   

def test_employee_age_is_valid():
    assert df["Age"].between(18, 65).all()


def test_monthly_income_is_non_negative():
    assert (df["MonthlyIncome"] >= 0).all()


def test_attrition_values_are_valid():
    assert df["Attrition"].isin(["Yes", "No"]).all()


def test_tenure_groups_are_created():
    assert df["TenureGroup"].notnull().all()


def test_experience_groups_are_created():
    assert df["ExperienceGroup"].notnull().all()
