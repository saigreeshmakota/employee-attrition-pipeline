
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text

from backend.database.connection import engine


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Employee Attrition Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Employee Attrition Analytics Dashboard")
st.caption("Workforce Analytics | Data Quality | Employee Insights")

st.divider()


# --------------------------------------------------
# 2. LOAD DATA FROM MYSQL
# --------------------------------------------------

@st.cache_data(ttl=60)
def load_employee_data():

    query = "SELECT * FROM employees"

    with engine.connect() as connection:
        df = pd.read_sql(text(query), connection)

    return df


try:
    df = load_employee_data()

except Exception as error:
    st.error(f"Unable to load employee data: {error}")
    st.stop()


if df.empty:
    st.warning("No employee records found in the database.")
    st.stop()


# --------------------------------------------------
# 3. DATA PREPARATION
# --------------------------------------------------

required_columns = [
    "EmployeeNumber",
    "Attrition",
    "MonthlyIncome",
    "Department",
    "Gender"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(f"Required columns missing: {missing_columns}")
    st.stop()


df["MonthlyIncome"] = pd.to_numeric(
    df["MonthlyIncome"],
    errors="coerce"
)

df["Attrition"] = df["Attrition"].astype("string").str.strip()
df["Department"] = df["Department"].astype("string").str.strip()
df["Gender"] = df["Gender"].astype("string").str.strip()

# Keep only records with valid employee IDs
df = df.dropna(subset=["EmployeeNumber"])


# --------------------------------------------------
# 4. SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

departments = sorted(
    df["Department"].dropna().unique().tolist()
)

selected_departments = st.sidebar.multiselect(
    "Select Department",
    options=departments,
    default=departments
)

genders = sorted(
    df["Gender"].dropna().unique().tolist()
)

selected_genders = st.sidebar.multiselect(
    "Select Gender",
    options=genders,
    default=genders
)

attrition_options = sorted(
    df["Attrition"].dropna().unique().tolist()
)

selected_attrition = st.sidebar.multiselect(
    "Select Attrition Status",
    options=attrition_options,
    default=attrition_options
)


filtered_df = df[
    df["Department"].isin(selected_departments)
    & df["Gender"].isin(selected_genders)
    & df["Attrition"].isin(selected_attrition)
].copy()


if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()


# --------------------------------------------------
# 5. KEY PERFORMANCE INDICATORS (KPIs)
# --------------------------------------------------

total_employees = filtered_df["EmployeeNumber"].nunique()

attrition_count = filtered_df.loc[
    filtered_df["Attrition"] == "Yes",
    "EmployeeNumber"
].nunique()

attrition_rate = (
    attrition_count / total_employees * 100
    if total_employees > 0 else 0
)

average_income = filtered_df["MonthlyIncome"].mean()


st.subheader("Workforce Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    f"{total_employees:,}"
)

col2.metric(
    "Employees Left",
    f"{attrition_count:,}"
)

col3.metric(
    "Attrition Rate",
    f"{attrition_rate:.2f}%"
)

col4.metric(
    "Average Monthly Income",
    f"₹{average_income:,.0f}"
)

st.caption(
    f"Showing {len(filtered_df):,} records after applying filters."
)

st.divider()


# --------------------------------------------------
# 6. DEPARTMENT-WISE ATTRITION
# --------------------------------------------------

st.subheader("Department-wise Attrition")

department_data = (
    filtered_df.groupby("Department")
    .agg(
        Total_Employees=("EmployeeNumber", "nunique"),
        Attrition_Count=(
            "Attrition",
            lambda values: (values == "Yes").sum()
        )
    )
    .reset_index()
)

department_data["Attrition_Rate"] = (
    department_data["Attrition_Count"]
    / department_data["Total_Employees"] * 100
)

fig_department = px.bar(
    department_data,
    x="Department",
    y="Attrition_Count",
    color="Department",
    title="Employee Attrition by Department",
    labels={
        "Attrition_Count": "Employees Left",
        "Department": "Department"
    },
    text="Attrition_Count"
)

st.plotly_chart(
    fig_department,
    use_container_width=True
)


# --------------------------------------------------
# 7. GENDER-WISE ATTRITION
# --------------------------------------------------

st.subheader("Gender-wise Attrition")

gender_data = (
    filtered_df.groupby("Gender")
    .agg(
        Total_Employees=("EmployeeNumber", "nunique"),
        Attrition_Count=(
            "Attrition",
            lambda values: (values == "Yes").sum()
        )
    )
    .reset_index()
)

fig_gender = px.pie(
    gender_data,
    names="Gender",
    values="Attrition_Count",
    title="Attrition Distribution by Gender",
    hole=0.4
)

st.plotly_chart(
    fig_gender,
    use_container_width=True
)


# --------------------------------------------------
# 8. ATTRITION STATUS DISTRIBUTION
# --------------------------------------------------

st.subheader("Employee Attrition Distribution")

attrition_data = (
    filtered_df["Attrition"]
    .value_counts()
    .reset_index()
)

attrition_data.columns = ["Attrition_Status", "Employee_Count"]

fig_attrition = px.bar(
    attrition_data,
    x="Attrition_Status",
    y="Employee_Count",
    color="Attrition_Status",
    title="Employees Who Stayed vs Left",
    text="Employee_Count"
)

st.plotly_chart(
    fig_attrition,
    use_container_width=True
)


# --------------------------------------------------
# 9. EMPLOYEE DATA PREVIEW
# --------------------------------------------------

st.subheader("Employee Data Preview")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)


# --------------------------------------------------
# 10. DATA QUALITY SUMMARY
# --------------------------------------------------

st.subheader("Dashboard Data Quality Summary")

quality_col1, quality_col2, quality_col3 = st.columns(3)

quality_col1.metric(
    "Records Loaded",
    f"{len(df):,}"
)

quality_col2.metric(
    "Unique Employee IDs",
    f"{df['EmployeeNumber'].nunique():,}"
)

quality_col3.metric(
    "Missing Monthly Income",
    f"{df['MonthlyIncome'].isna().sum():,}"
)


st.divider()

st.caption(
    "Employee Attrition Analytics | "
    "Python • Streamlit • Plotly • MySQL"
)
