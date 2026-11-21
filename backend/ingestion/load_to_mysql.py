
import pandas as pd
from sqlalchemy import text

from backend.database.connection import engine

# Locate the transformed dataset
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

CSV_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "transformed_employee_attrition.csv"
)

TABLE_NAME = "employees"


def load_employee_data():
    print("Reading transformed employee data...")

    df = pd.read_csv(CSV_FILE)

    print("CSV records:", len(df))

    # Check whether the target table is empty.
    with engine.connect() as connection:
        existing_count = connection.execute(
            text("SELECT COUNT(*) FROM employees")
        ).scalar_one()

    if existing_count > 0:
        raise RuntimeError(
            f"Target table already contains {existing_count} records. "
            "Loading stopped to prevent duplicate insertion."
        )

    print("Loading records into MySQL...")

    df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=500
    )

    with engine.connect() as connection:
        loaded_count = connection.execute(
            text("SELECT COUNT(*) FROM employees")
        ).scalar_one()

    print("CSV records:", len(df))
    print("MySQL records:", loaded_count)

    assert len(df) == loaded_count, (
        "Source and target record counts do not match!"
    )

    print("Data loading completed successfully!")


if __name__ == "__main__":
    load_employee_data()
