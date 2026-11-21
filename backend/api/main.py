
from fastapi import FastAPI, HTTPException
from sqlalchemy import text

from backend.database.connection import engine

app = FastAPI(
    title="Employee Attrition Analytics API",
    description="API for employee attrition data and analytics",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Employee Attrition Analytics API is running"
    }


@app.get("/employees")
def get_employees():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM employees LIMIT 100")
            )

            employees = [
                dict(row._mapping) for row in result
            ]

        return {
            "status": "success",
            "total_records": len(employees),
            "data": employees
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve employee records"
        )
