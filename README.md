# Employee Attrition Analytics – End-to-End Data Quality & Testing Framework

## Project Overview

An end-to-end data engineering and quality assurance project designed to process, validate, test, and analyze employee attrition data.

The project demonstrates how data quality can be maintained across an ETL pipeline, MySQL database, REST API, and analytics dashboard using automated testing and reconciliation techniques.

## Business Problem

Organizations need reliable employee data to understand workforce attrition. Inconsistent records, missing values, duplicate employee IDs, and incorrect transformations can lead to inaccurate business reports.

This project addresses these challenges by implementing data validation, database testing, source-to-target reconciliation, API testing, and dashboard verification.

## Project Objectives

- Build an end-to-end ETL pipeline using Python and Pandas.
- Validate data quality and business rules.
- Store transformed employee records in MySQL.
- Perform SQL-based data quality testing.
- Implement source-to-target reconciliation.
- Develop REST APIs using FastAPI.
- Build an interactive analytics dashboard using Streamlit.
- Automate testing using Pytest.
- Generate HTML test execution reports.
## System Architecture

The project follows an end-to-end data processing and quality assurance workflow.

```text
Raw Employee Dataset (CSV)
          |
          v
   Data Ingestion
          |
          v
 Data Profiling & Validation
          |
          v
 Data Cleaning & Transformation
          |
          v
   Transformed Dataset
          |
          v
      MySQL Database
          |
     +----+-----+
     |          |
     v          v
  FastAPI    Streamlit
     |       Dashboard
     v
 API Testing
     |
     v
  Pytest Automation
     |
     v
 HTML Test Reports
 ## Quality Assurance & Testing

The project uses a combination of automated and database-level testing techniques.

### 1. Data Quality Testing
- Missing value validation
- Duplicate record detection
- Employee ID uniqueness
- Age and income validation
- Business rule validation
- Data type checks

### 2. ETL Testing
- Source and target record count validation
- Transformation validation
- Derived column verification
- Employee ID reconciliation
- Data consistency checks

### 3. SQL Testing
- Database record count validation
- Duplicate employee ID checks
- Null value checks
- Invalid business value checks
- Department and job role validation

### 4. API Testing
- Endpoint response validation
- Database failure handling
- API data quality validation
- API record limit validation
- API-to-MySQL reconciliation
- Field-level data comparison

### 5. Dashboard Testing
- KPI validation
- Department-wise attrition validation
- Gender-wise attrition validation
- Filter functionality testing
- Dashboard-to-SQL result comparison

## Test Execution Results

| Testing Area | Result |
|---|---|
| Complete automated test suite | 22 Passed |
| Failed tests | 0 |
| Warnings | 1 |
| API automated tests | 7 Passed |

### Test Reports

- API Report: `reports/api_test_report.html`
- Complete QA Report: `reports/full_qa_test_report.html`
- SQL Validation Evidence: `reports/sql_validation_output.txt`
- Reconciliation Evidence: `reports/reconciliation/`
## Installation & Setup

### Prerequisites

- Python 3.14+
- MySQL Server
- Git
- VS Code

### 1. Clone the Repository

```bash
git clone https://github.com/saigreeshmakota/employee-attrition-pipeline.git
cd employee-attrition-pipeline
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=employee_attrition_db
```

Use your own MySQL credentials. Never commit `.env` to GitHub.

### 5. Run the API

```bash
python -m uvicorn backend.api.main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

### 6. Run the Dashboard

Open a separate terminal:

```bash
python -m streamlit run frontend/dashboard/app.py
```

### 7. Run Automated Tests

```bash
python -m pytest -v
```

### 8. Generate the HTML Test Report

```bash
python -m pytest -v --html=reports/full_qa_test_report.html --self-contained-html
```