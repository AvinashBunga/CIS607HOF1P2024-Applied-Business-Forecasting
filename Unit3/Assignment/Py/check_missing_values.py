# Import necessary libraries
import pandas as pd

# Define the file path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Clean_Dataset.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Check for missing values in each column
print("\nMissing values in each column:")
missing_values = data.isnull().sum()
print(missing_values)

# Check the percentage of missing values in each column
print("\nPercentage of missing values in each column:")
missing_percentage = (data.isnull().sum() / len(data)) * 100
print(missing_percentage)

# Display columns with missing values
missing_cols = missing_values[missing_values > 0]
if not missing_cols.empty:
    print("\nColumns with missing values:")
    print(missing_cols)
else:
    print("\nNo missing values found in the dataset.")
