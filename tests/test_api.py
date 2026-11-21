
from fastapi.testclient import TestClient

from backend.api.main import app
from unittest.mock import patch

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Employee Attrition Analytics API is running"
    }

def test_get_employees_endpoint():
    response = client.get("/employees")

    assert response.status_code == 200

    result = response.json()

    assert result["status"] == "success"
    assert result["total_records"] == 100
    assert isinstance(result["data"], list)

    assert len(result["data"]) == 100
    assert "EmployeeNumber" in result["data"][0]

def test_employees_endpoint_database_failure():
    with patch(
        "backend.api.main.engine.connect",
        side_effect=Exception("Database connection failed")
    ):
        response = client.get("/employees")

    assert response.status_code == 500

    assert response.json() == {
        "detail": "Unable to retrieve employee records"
    }

def test_employee_api_data_quality():
    response = client.get("/employees")

    assert response.status_code == 200

    employees = response.json()["data"]

    employee_ids = [
        employee["EmployeeNumber"]
        for employee in employees
    ]

    assert all(employee_id is not None for employee_id in employee_ids)
    assert len(employee_ids) == len(set(employee_ids))

    for employee in employees:
        assert employee["MonthlyIncome"] >= 0
        assert employee["Attrition"] in ["Yes", "No"]
def test_employee_api_record_limit():
    response = client.get("/employees")

    assert response.status_code == 200

    data = response.json()

    assert data["total_records"] <= 100
    assert len(data["data"]) <= 100

from sqlalchemy import text
from backend.database.connection import engine


def test_api_employee_ids_match_mysql():
    response = client.get("/employees")

    assert response.status_code == 200

    api_ids = [
        employee["EmployeeNumber"]
        for employee in response.json()["data"]
    ]

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT EmployeeNumber
                FROM employees
                ORDER BY EmployeeNumber
                LIMIT 100
            """)
        )

        mysql_ids = [row[0] for row in result]

    assert api_ids == mysql_ids

def test_api_employee_fields_match_mysql():
    response = client.get("/employees")

    assert response.status_code == 200

    api_records = response.json()["data"]

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT EmployeeNumber, MonthlyIncome,
                       Department, Attrition, JobRole
                FROM employees
                ORDER BY EmployeeNumber
                LIMIT 100
            """)
        )

        mysql_records = [dict(row._mapping) for row in result]

    assert len(api_records) == len(mysql_records)

    for api_record, mysql_record in zip(api_records, mysql_records):
        assert api_record["EmployeeNumber"] == mysql_record["EmployeeNumber"]
        assert api_record["MonthlyIncome"] == mysql_record["MonthlyIncome"]
        assert api_record["Department"] == mysql_record["Department"]
        assert api_record["Attrition"] == mysql_record["Attrition"]
        assert api_record["JobRole"] == mysql_record["JobRole"]

