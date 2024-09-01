# Import necessary libraries
import pandas as pd

# Define the file path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Clean_Dataset.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Display the initial data types of all columns
print("Data types of all columns:")
print(data.dtypes)

# Display the first few rows to get an overview of the dataset
print("\nFirst few rows of the dataset:")
print(data.head())

# Check for any non-numeric values in numerical columns
print("\nChecking for non-numeric values in potential numerical columns:")
for col in data.select_dtypes(include=['object']).columns:
    try:
        # Attempt to convert to numeric to identify non-numeric issues
        pd.to_numeric(data[col], errors='raise')
        print(f"No non-numeric values found in column '{col}'.")
    except ValueError:
        print(f"Non-numeric values found in column '{col}'. Here are some examples:")
        print(data[col].unique()[:5])  # Display a few unique values for review
