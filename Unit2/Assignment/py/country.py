import pandas as pd

# Load the dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData_Cleaned.xlsx'
apple_data_cleaned = pd.read_excel(file_path)

# Filter the dataset to include only the iPhone models of interest
iphone_models = ['iPhone 3', 'iPhone 4', 'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8']

# Filter the data for these specific models
filtered_data = apple_data_cleaned[apple_data_cleaned['iPhone model '].isin(iphone_models)]

# Create a pivot table to count occurrences of each model per country
pivot_table = filtered_data.pivot_table(index='iPhone model ', columns='Country of Release', values='Date of Release', aggfunc='count')

# Filter to find countries that have data for all the specified iPhone models
matching_countries = pivot_table.dropna(axis=1).columns.tolist()

# Display the matching countries
print("Countries with complete data for iPhone 3 to iPhone 8:")
print(matching_countries)
