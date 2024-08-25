import pandas as pd

# Load the cleaned dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData_Cleaned.xlsx'
apple_data_cleaned = pd.read_excel(file_path)

# Print unique values in 'Country of Release' to check how 'USA' is represented
unique_countries = apple_data_cleaned['Country of Release'].unique()
print("Unique values in 'Country of Release':")
print(unique_countries)
