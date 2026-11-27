import pandera as pa
from pandera import Column, Check


EMPLOYEE_SCHEMA = pa.DataFrameSchema(
    {
        "EmployeeNumber": Column(int, Check.gt(0), nullable=False, unique=True),
        "Age": Column(int, Check.in_range(18, 65), nullable=False),
        "Attrition": Column(str, Check.isin(["Yes", "No"]), nullable=False),
        "MonthlyIncome": Column(int, Check.ge(0), nullable=False),
        "TotalWorkingYears": Column(int, Check.ge(0), nullable=False),
        "YearsAtCompany": Column(int, Check.ge(0), nullable=False),
    },
    strict=False,
    coerce=True,
)


def validate_employee_dataframe(dataframe):
    """Validate required employee fields and core workforce business rules."""
    return EMPLOYEE_SCHEMA.validate(dataframe, lazy=True)
