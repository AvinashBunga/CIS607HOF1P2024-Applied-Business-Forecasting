import pandas as pd

# Load the dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/USA_AppleData.xlsx'
usa_data = pd.read_excel(file_path)

# Convert 'Date of Release' to datetime format
usa_data['Date of Release'] = pd.to_datetime(usa_data['Date of Release'])

# Calculate the time differences in days between consecutive releases
usa_data['Time Between Releases (days)'] = usa_data['Date of Release'].diff().dt.days

# Drop the first row with NaN value in 'Time Between Releases (days)'
usa_data_cleaned = usa_data.dropna(subset=['Time Between Releases (days)'])

# Display the cleaned data with calculated time differences
print("Cleaned Data with Time Differences:")
print(usa_data_cleaned)

# save the cleaned data to a new file
output_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/USA_AppleData_TimeDifferences.xlsx'
usa_data_cleaned.to_excel(output_path, index=False)
print(f"\nData with time differences saved to: {output_path}")
