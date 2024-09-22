# Import necessary libraries
import pandas as pd

# Load the motor vehicle crash dataset
data_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Cleaned_Motor_Vehicle_Collisions.csv'  # Update this path as needed
data = pd.read_csv(data_path)

# Convert 'CRASH DATE' to datetime format
data['CRASH DATE'] = pd.to_datetime(data['CRASH DATE'])

# Extract year and month from 'CRASH DATE'
data['Year'] = data['CRASH DATE'].dt.year
data['Month'] = data['CRASH DATE'].dt.month

# Create a dataframe of all expected year-month combinations
all_years = data['Year'].unique()
expected_months = pd.DataFrame([(year, month) for year in all_years for month in range(1, 13)], columns=['Year', 'Month'])

# Group by year and month to get the actual year-month combinations in the data
actual_months = data.groupby(['Year', 'Month']).size().reset_index(name='Incident_Count')

# Merge expected months with actual months to find missing months
missing_months = pd.merge(expected_months, actual_months, on=['Year', 'Month'], how='left', indicator=True)

# Filter out rows where the month is missing
missing_months = missing_months[missing_months['_merge'] == 'left_only']

# Check if any missing months were found and print the results
if not missing_months.empty:
    print("The following months are missing in the data:")
    print(missing_months[['Year', 'Month']])
else:
    print("All months are covered for every year in the data.")
