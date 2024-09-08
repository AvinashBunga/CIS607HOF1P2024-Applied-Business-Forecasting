import pandas as pd

# File path to the dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Motor_Vehicle_Collisions_-_Crashes.csv'

# Load the dataset
try:
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Display the first few rows to understand the structure of the data
    print("First 5 rows of the dataset:")
    print(data.head())

    # Get basic information about the dataset (columns, data types, non-null counts)
    print("\nDataset Information:")
    print(data.info())

    # Check for missing values
    missing_values = data.isnull().sum()
    print("\nMissing Values in Each Column:")
    print(missing_values[missing_values > 0])

    # Summary statistics for numerical columns
    print("\nSummary Statistics for Numerical Columns:")
    print(data.describe())

    # Check for duplicate rows
    duplicates = data.duplicated().sum()
    print(f"\nNumber of Duplicate Rows: {duplicates}")

    # Check the unique values in key columns like crash date and contributing factors
    print("\nUnique Values in Key Columns:")
    print(f"Unique crash dates: {data['CRASH DATE'].nunique()}")
    print(f"Unique contributing factors (vehicle 1): {data['CONTRIBUTING FACTOR VEHICLE 1'].nunique()}")

    # Check the range of dates in the data (if date is in string format, parse it as datetime)
    data['CRASH DATE'] = pd.to_datetime(data['CRASH DATE'], errors='coerce')
    print(f"\nDate Range of the Data: {data['CRASH DATE'].min()} to {data['CRASH DATE'].max()}")

except Exception as e:
    print(f"An error occurred: {e}")
