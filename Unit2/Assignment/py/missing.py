import pandas as pd

# Updated file path without spaces
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData.xlsx'

# Load the dataset
apple_data = pd.read_excel(file_path)

# Check for missing values in each column
missing_values = apple_data.isnull().sum()

# Display the missing values count
print("Missing values in each column:")
print(missing_values)

# Optionally, display the total number of missing values
total_missing = missing_values.sum()
print(f"\nTotal missing values in the dataset: {total_missing}") 
