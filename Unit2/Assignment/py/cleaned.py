import pandas as pd

# Updated file path without spaces
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData.xlsx'

# Load the dataset
apple_data = pd.read_excel(file_path)

# Check for missing values in each column
print("Missing values before cleaning:")
print(apple_data.isnull().sum())

# Drop rows with any missing values
apple_data_cleaned = apple_data.dropna()

# Verify if the missing values have been handled
print("\nMissing values after cleaning:")
print(apple_data_cleaned.isnull().sum())

# Optionally, save the cleaned dataset to a new file
apple_data_cleaned.to_excel('/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData_Cleaned.xlsx', index=False)
