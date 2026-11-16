import pandas as pd 

#Define the data set path 
file_path ="data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"

#read the csv file 
df = pd.read_csv(file_path)

#display the first 5 rows of the data frame 
print("First 5 records of the data:")
print(df.head())

#display the data set dimensions 
print("Data set dimensions:")
print(df.shape)

#display the columns 
print("column names:")
print(df.columns.to_list())# tolist convert the column names to the list 



## Data profilling 

print("\n Data information:")
df.info()

print("\n employee data statistics:")
print(df.describe())

# check the missing values in the data set 

print("\n missing values in the data set:")
print(df.isnull().sum())

#check the duplicate records 
print("\n duplicate records in the data set:")
duplicate_count =df.duplicated().sum()
print("\n duplicate records in the data set:" ,duplicate_count)

print("\n--- DATA TYPES ---")

print(df.dtypes)

print("\n--- UNIQUE VALUES ---")
print("Attrition:", df["Attrition"].unique())
print("Department:", df["Department"].unique())
print("Gender:", df["Gender"].unique())
print("OverTime:", df["OverTime"].unique())

print ('\n --- Business rules validation ----')

#rule1 - checks the employee age ()
invalid_age = df[~df["Age"].between(18,65)]
print("Invalid age records:",len(invalid_age))

#rule2 - check the employee monthly income
invalid_income = df[df["MonthlyIncome"] < 0]
print("Invalid monthly income records:",len(invalid_income))

# Rule 3: Check negative working years
invalid_experience = df[df["TotalWorkingYears"] < 0]
print("Negative working years:", len(invalid_experience))

# Rule 4: Check invalid attrition values
invalid_attrition = df[~df["Attrition"].isin(["Yes", "No"])]
print("Invalid attrition records:", len(invalid_attrition))

# Rule 5: Check duplicate employee numbers
duplicate_ids = df[df["EmployeeNumber"].duplicated()]
print("Duplicate employee IDs:", len(duplicate_ids))

# Check years at company against total working years

invalid_experience = df[
    df["YearsAtCompany"] > df["TotalWorkingYears"]
]

print(
    "Invalid company experience records:",
    len(invalid_experience)
)