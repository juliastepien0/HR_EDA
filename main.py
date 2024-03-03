import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

hr_df = pd.read_csv('Human_Resources.csv')
print(hr_df.head())

print(hr_df.info())
#35 columns in total, MonthlyIncome, Department, EducationField, EmployeeNumber, Gender, JobRole, MaritalStatus, MonthlyRate
#PercentSalaryHike, PerformanceRating with null values

print(hr_df.describe())
