# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the cleaned data file
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Cleaned_Updated.csv"  # Update with your actual file path if needed
data = pd.read_csv(file_path)

# Display the first few rows to ensure the data is loaded correctly
print("First few rows of the dataset:")
print(data.head())

# Step 1: Perform the 80-20 split
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Display the number of records in each split
print(f"\nNumber of records in the training set: {len(train_data)}")
print(f"Number of records in the testing set: {len(test_data)}")

# Step 2: Save the split datasets
train_data_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Train.csv"
test_data_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Test.csv"

train_data.to_csv(train_data_path, index=False)
test_data.to_csv(test_data_path, index=False)

print(f"\nTraining set saved as: {train_data_path}")
print(f"Testing set saved as: {test_data_path}")
