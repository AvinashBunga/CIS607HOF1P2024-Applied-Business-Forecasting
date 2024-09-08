import pandas as pd

# Load the dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Assignment/MentalHealthSurvey.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print("First few rows of the dataset:")
print(data.head())

# Check data types of each column
print("\nData types of each column:")
print(data.dtypes)

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Display unique values for each column to inspect further
for column in data.columns:
    unique_values = data[column].unique()
    print(f"\nUnique values in '{column}' ({len(unique_values)} unique values):")
    print(unique_values[:10])  # Show up to the first 10 unique values for inspection
