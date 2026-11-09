import pandas as pd 

from backend.ingestion.csv_loader import load_employee_data

def profile_employee_data():
    df = load_employee_data()
    print("Total rows and columns:")
    rows ,columns = df.shape
    print("Data profile:")
    print(f"Total rows: {rows}")
    print(f"Total columns: {columns}")
if __name__ == "__main__" :
    profile_employee_data()
