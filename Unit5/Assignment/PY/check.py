# Import necessary libraries
import pandas as pd

# Load your data file from the specified path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX.csv"  # Update with the exact file name if different
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(data.head())

# Display the summary of the dataset including column names, data types, and non-null counts
print("\nSummary of the dataset:")
print(data.info())

# Check for missing values in each column
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Calculate the percentage of missing data for each column
missing_percentage = (missing_values / len(data)) * 100
print("\nPercentage of missing data in each column:")
print(missing_percentage)

# Check data types of each column
print("\nData types of each column:")
print(data.dtypes)

# Summary statistics of numerical columns to check data ranges and distributions
print("\nSummary statistics of numerical columns:")
print(data.describe())

# Check for any columns that might have incorrect data types (e.g., numbers stored as objects)
# Attempting to convert object types to numeric where possible
for col in data.columns:
    if data[col].dtype == 'object':
        try:
            data[col] = pd.to_numeric(data[col])
            print(f"Column '{col}' converted to numeric.")
        except ValueError:
            print(f"Column '{col}' could not be converted to numeric.")

# Visual check for any potential issues with data distribution, such as zeros or outliers
print("\nChecking for rows with zero values (if relevant):")
print((data == 0).sum())

# Check for duplicates
print("\nChecking for duplicate rows in the dataset:")
duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Recommendations based on initial data checks
if missing_percentage.max() > 20:
    print("\nWarning: Some columns have more than 20% missing data, consider imputing or dropping these columns.")
else:
    print("\nData looks manageable with respect to missing values.")

print("\nInitial data check complete. Next step: Data cleaning and preprocessing.")
