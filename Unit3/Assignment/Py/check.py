# Import necessary libraries
import pandas as pd

# Define the file path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Selective_Encoded_Dataset.csv"

# Load the encoded dataset
data = pd.read_csv(file_path)

# Display the first few rows to inspect the data
print("First few rows of the encoded dataset:")
print(data.head())

# Check data types to ensure correct encoding
print("\nData types of the columns:")
print(data.dtypes)

# Check for any missing values in the dataset
print("\nChecking for missing values:")
missing_values = data.isnull().sum()
print(missing_values[missing_values > 0])

# Explore correlations with the target variable (price)
correlations = data.corr()['price'].sort_values(ascending=False)
print("\nCorrelation of features with 'price':")
print(correlations)
