import pandas as pd
from sqlalchemy import text

from backend.database.connection import engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "processed" / "transformed_employee_attrition.csv"
TABLE_NAME = "employees"


def load_employee_data():
    print("Reading transformed employee data...")
    df = pd.read_csv(CSV_FILE)
    print("CSV records:", len(df))

    # Create the target table from the transformed dataframe schema if needed.
    # This keeps a clean MySQL database usable on the first pipeline run.
    df.head(0).to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="append",
        index=False,
    )

    with engine.connect() as connection:
        existing_count = connection.execute(
            text("SELECT COUNT(*) FROM employees")
        ).scalar_one()

    if existing_count > 0:
        raise RuntimeError(
            f"Target table already contains {existing_count} records. "
            "Loading stopped to prevent duplicate insertion. Use an empty "
            "dedicated target table for a fresh full-pipeline run."
        )

    print("Loading records into MySQL...")
    df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=500,
    )

    with engine.connect() as connection:
        loaded_count = connection.execute(
            text("SELECT COUNT(*) FROM employees")
        ).scalar_one()

    print("CSV records:", len(df))
    print("MySQL records:", loaded_count)

    if len(df) != loaded_count:
        raise AssertionError("Source and target record counts do not match!")

    print("Data loading completed successfully!")


if __name__ == "__main__":
    load_employee_data()
