import pandas as pd

# Load the dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData_Cleaned.xlsx'
apple_data_cleaned = pd.read_excel(file_path)

# Select the countries for comparison (USA and Hong Kong)
selected_countries = ['US', 'Hong Kong']

# Filter the data for the selected countries and iPhone models
iphone_models = ['iPhone 3', 'iPhone 4', 'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8']
filtered_data = apple_data_cleaned[apple_data_cleaned['Country of Release'].isin(selected_countries) & apple_data_cleaned['iPhone model '].isin(iphone_models)]

# Convert 'Date of Release' to datetime format
filtered_data['Date of Release'] = pd.to_datetime(filtered_data['Date of Release'])

# Sort the data by 'Country of Release' and 'Date of Release'
filtered_data = filtered_data.sort_values(by=['Country of Release', 'Date of Release'])

# Calculate the time differences in days between consecutive releases for each country
filtered_data['Time Between Releases (days)'] = filtered_data.groupby('Country of Release')['Date of Release'].diff().dt.days

# Drop rows with NaN values resulting from the diff() operation
filtered_data = filtered_data.dropna(subset=['Time Between Releases (days)'])

# Save the prepared data to a new Excel file
output_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/USA_HK_AppleData_TimeDifferences.xlsx'
filtered_data.to_excel(output_path, index=False)

# Display the first few rows of the prepared data
print(filtered_data.head())
