import pandas as pd

# Load the dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData_Cleaned.xlsx'
apple_data_cleaned = pd.read_excel(file_path)

# Select the countries for comparison: USA and Canada
selected_countries = ['US', 'Canada']

# Filter the data for the selected countries and specific iPhone models
iphone_models = ['iPhone 3', 'iPhone 4', 'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8']
filtered_data = apple_data_cleaned[apple_data_cleaned['Country of Release'].isin(selected_countries) & 
                                   apple_data_cleaned['iPhone model '].isin(iphone_models)]

# Convert 'Date of Release' to datetime format and sort by country and release date
filtered_data['Date of Release'] = pd.to_datetime(filtered_data['Date of Release'])
filtered_data = filtered_data.sort_values(by=['Country of Release', 'Date of Release'])

# Calculate the time differences in days between consecutive releases for each country
filtered_data['Time Between Releases (days)'] = filtered_data.groupby('Country of Release')['Date of Release'].diff().dt.days

# Drop rows with NaN values resulting from the diff() operation
filtered_data_cleaned = filtered_data.dropna(subset=['Time Between Releases (days)'])

# Save the cleaned data to a new Excel file for analysis in R
output_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/USA_Canada_AppleData_TimeDifferences.xlsx'
filtered_data_cleaned.to_excel(output_path, index=False)

# Display the cleaned data
print(filtered_data_cleaned.head())
print(f"Cleaned data saved to: {output_path}")
