import pandas as pd

# Step 1: Load the Data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car Features and MSRP.csv'
car_data = pd.read_csv(file_path)

# Display rows with missing values
missing_data = car_data[car_data.isnull().any(axis=1)]
print("Rows with missing values:\n")
print(missing_data)