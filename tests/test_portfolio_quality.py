import pandas as pd
import pytest

from backend.validation.schema import validate_employee_dataframe
from backend.modeling.train_attrition import build_preprocessor


def valid_employee_frame():
    return pd.DataFrame({
        "EmployeeNumber": [1, 2],
        "Age": [29, 41],
        "Attrition": ["No", "Yes"],
        "MonthlyIncome": [4000, 5200],
        "TotalWorkingYears": [6, 15],
        "YearsAtCompany": [3, 8],
        "Department": ["Sales", "Research & Development"],
    })


def test_valid_employee_rows_pass_schema():
    validated = validate_employee_dataframe(valid_employee_frame())
    assert len(validated) == 2


def test_invalid_attrition_value_fails_schema():
    frame = valid_employee_frame()
    frame.loc[0, "Attrition"] = "Maybe"
    with pytest.raises(Exception):
        validate_employee_dataframe(frame)


def test_employee_ids_must_be_unique():
    frame = valid_employee_frame()
    frame.loc[1, "EmployeeNumber"] = 1
    with pytest.raises(Exception):
        validate_employee_dataframe(frame)


def test_age_outside_business_range_fails():
    frame = valid_employee_frame()
    frame.loc[0, "Age"] = 15
    with pytest.raises(Exception):
        validate_employee_dataframe(frame)


def test_preprocessor_detects_numeric_and_categorical_columns():
    frame = valid_employee_frame().drop(columns=["EmployeeNumber", "Attrition"])
    preprocessor = build_preprocessor(frame)
    transformed = preprocessor.fit_transform(frame)
    assert transformed.shape[0] == 2
    assert transformed.shape[1] > 0
