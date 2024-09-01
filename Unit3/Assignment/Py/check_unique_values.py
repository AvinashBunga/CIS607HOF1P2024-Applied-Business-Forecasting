# Import necessary libraries
import pandas as pd

# Define the file path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Clean_Dataset.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Display the first few rows to confirm the data load
print("First few rows of the dataset:")
print(data.head())

# Check the number of unique values in each column
print("\nNumber of unique values in each column:")
unique_counts = data.nunique()
print(unique_counts)

# Display columns with high unique counts
print("\nColumns with more than 20 unique values (potentially high cardinality):")
high_cardinality_columns = unique_counts[unique_counts > 20]
print(high_cardinality_columns)
