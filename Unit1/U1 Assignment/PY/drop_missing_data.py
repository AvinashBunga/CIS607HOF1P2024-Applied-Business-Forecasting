import pandas as pd

#Load the Data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car Features and MSRP.csv'
car_data = pd.read_csv(file_path)

# Step 1: Check the total number of rows before dropping missing data
total_rows_before = car_data.shape[0]
print(f"Total number of rows before dropping missing data: {total_rows_before}")

# Step 2: Drop rows with missing data
car_data_cleaned = car_data.dropna()

# Step 3: Check the total number of rows after dropping missing data
total_rows_after = car_data_cleaned.shape[0]
print(f"Total number of rows after dropping missing data: {total_rows_after}")

# Save the cleaned data to a new CSV file
car_data_cleaned.to_csv('/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned.csv', index=False)

