import pandas as pd

# Load the new dataset for 2007-2017
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned_2007_2017.csv'
car_data_filtered = pd.read_csv(file_path)

# Segment the data by Vehicle Size and calculate descriptive statistics for MSRP
msrp_by_vehicle_size = car_data_filtered.groupby('Vehicle Size')['MSRP'].agg(['count', 'mean', 'std', 'min', 'median', 'max'])

# Print the descriptive statistics
print("Descriptive statistics for MSRP by Vehicle Size (2007-2017):\n")
print(msrp_by_vehicle_size)
