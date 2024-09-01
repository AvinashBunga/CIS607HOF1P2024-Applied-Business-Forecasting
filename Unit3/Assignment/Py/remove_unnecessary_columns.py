# Import necessary libraries
import pandas as pd

# Define the file path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Clean_Dataset.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Display the first few rows of the dataset before removing the column
print("Dataset before removing unnecessary columns:")
print(data.head())

# Remove the unnecessary 'Unnamed: 0' column
if 'Unnamed: 0' in data.columns:
    data = data.drop(columns=['Unnamed: 0'])
    print("\n'Unnamed: 0' column removed successfully.")
else:
    print("\n'Unnamed: 0' column not found in the dataset.")

# Display the first few rows after removing the column
print("\nDataset after removing unnecessary columns:")
print(data.head())

# Save the updated dataset back to the original file path
data.to_csv(file_path, index=False)
print(f"\nUpdated dataset saved to {file_path}")
