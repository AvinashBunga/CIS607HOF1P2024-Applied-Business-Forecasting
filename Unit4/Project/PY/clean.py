import pandas as pd

# File paths
input_file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Motor_Vehicle_Collisions_-_Crashes.csv'
output_file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Cleaned_Motor_Vehicle_Collisions.csv'

# Load the dataset
data = pd.read_csv(input_file_path)

# Data Cleaning Steps

# 1. Drop rows with missing critical information (e.g., crash date, latitude, longitude)
data = data.dropna(subset=['CRASH DATE', 'LATITUDE', 'LONGITUDE'])

# 2. Drop rows with missing values in contributing factors and vehicle types
columns_to_check = ['CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2',
                    'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4',
                    'CONTRIBUTING FACTOR VEHICLE 5', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2']
data = data.dropna(subset=columns_to_check)

# 3. Convert CRASH DATE to datetime format
data['CRASH DATE'] = pd.to_datetime(data['CRASH DATE'], errors='coerce')

# 4. Remove duplicates
data = data.drop_duplicates()

# 5. Save the cleaned dataset
data.to_csv(output_file_path, index=False)

# Statistics of the Cleaned Data
print("First 5 rows of the cleaned dataset:")
print(data.head())

print("\nCleaned Dataset Information:")
print(data.info())

missing_values_cleaned = data.isnull().sum()
print("\nMissing Values in Each Column (Cleaned Data):")
print(missing_values_cleaned[missing_values_cleaned > 0])

print("\nSummary Statistics for Numerical Columns (Cleaned Data):")
print(data.describe())

duplicates_cleaned = data.duplicated().sum()
print(f"\nNumber of Duplicate Rows in Cleaned Data: {duplicates_cleaned}")

print("\nUnique Values in Key Columns (Cleaned Data):")
print(f"Unique crash dates: {data['CRASH DATE'].nunique()}")
print(f"Unique contributing factors (vehicle 1): {data['CONTRIBUTING FACTOR VEHICLE 1'].nunique()}")

print(f"\nDate Range of the Cleaned Data: {data['CRASH DATE'].min()} to {data['CRASH DATE'].max()}")
