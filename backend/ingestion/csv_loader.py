import pandas as pd 

def load_employee_data():
    file_path="data/raw/WA_Fn-UseC_-HR-Employee-Attrition 2.csv"
    df=pd.read_csv(file_path)
    return df
if __name__ == "__main__":

    employee_df=load_employee_data()

    print ("Dataset loaded successfully")

    print("/nFirst 5 records")
    print(employee_df.head())

    print("/nDataset dimensions:")
    print(employee_df.shape)

    print("/n column names :")
    print(employee_df.columns.tolist())