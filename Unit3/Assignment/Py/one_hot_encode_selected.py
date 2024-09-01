# Import necessary libraries
import pandas as pd

# Define the file paths
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Clean_Dataset.csv"
output_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Selective_Encoded_Dataset.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Display the first few rows to confirm the data load
print("First few rows of the dataset before encoding:")
print(data.head())

# Columns selected for one-hot encoding
columns_to_encode = ['airline', 'source_city', 'departure_time', 'stops', 
                     'arrival_time', 'destination_city', 'class']

# Apply one-hot encoding to the selected lower cardinality columns
data_encoded = pd.get_dummies(data, columns=columns_to_encode)

# Display the first few rows after encoding
print("\nFirst few rows of the dataset after one-hot encoding:")
print(data_encoded.head())

# Save the updated dataset to a new file
data_encoded.to_csv(output_path, index=False)
print(f"\nSelective encoded dataset saved to {output_path}")
