import pandas as pd

# Load the cleaned data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned.csv'
car_data_cleaned = pd.read_csv(file_path)

# Step 3: Segment the data by Vehicle Size and calculate descriptive statistics for MSRP
msrp_by_vehicle_size = car_data_cleaned.groupby('Vehicle Size')['MSRP'].agg(['count', 'mean', 'std', 'min', 'median', 'max'])

# Print the descriptive statistics
print("Descriptive statistics for MSRP by Vehicle Size:\n")
print(msrp_by_vehicle_size)
