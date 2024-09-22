import pandas as pd

#Load the Data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car Features and MSRP.csv'
car_data = pd.read_csv(file_path)

# Step 1: Check the total number of rows before dropping missing data
total_rows_before = car_data.shape[0]
print(f"Total number of rows before dropping missing data: {total_rows_before}")