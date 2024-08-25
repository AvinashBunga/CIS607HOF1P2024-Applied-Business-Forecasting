import pandas as pd

# Load the cleaned dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/AppleData_Cleaned.xlsx'
apple_data_cleaned = pd.read_excel(file_path)

# Filter the dataset for only US release dates
usa_data = apple_data_cleaned[apple_data_cleaned['Country of Release'] == 'US']

# Drop rows with NaN values in 'Date of Release' if they exist
usa_data = usa_data.dropna(subset=['Date of Release'])

# Sort by 'Date of Release' to ensure correct chronological order
usa_data.sort_values(by='Date of Release', inplace=True)

# Save the filtered US data
output_path = '/Users/avinash/Desktop/CIS/CIS607/Unit2/Assignment/py/USA_AppleData.xlsx'
usa_data.to_excel(output_path, index=False)

print(f"Filtered US data saved to: {output_path}")

# Display the first few rows of the US data
print(usa_data.head())
