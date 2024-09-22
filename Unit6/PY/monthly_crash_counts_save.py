# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the motor vehicle crash dataset
data_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Cleaned_Motor_Vehicle_Collisions.csv'  # Update this path as needed
data = pd.read_csv(data_path)

# Convert 'CRASH DATE' to datetime format
data['CRASH DATE'] = pd.to_datetime(data['CRASH DATE'])

# Extract year and month from 'CRASH DATE'
data['Year'] = data['CRASH DATE'].dt.year
data['Month'] = data['CRASH DATE'].dt.month

# Find years with missing months
all_years = data['Year'].unique()
expected_months = pd.DataFrame([(year, month) for year in all_years for month in range(1, 13)], columns=['Year', 'Month'])
actual_months = data.groupby(['Year', 'Month']).size().reset_index(name='Incident_Count')
missing_months = pd.merge(expected_months, actual_months, on=['Year', 'Month'], how='left', indicator=True)
missing_months = missing_months[missing_months['_merge'] == 'left_only']

# Get the list of years with missing months
years_with_missing_months = missing_months['Year'].unique()

# Filter out the years with missing months from the original data
data_filtered = data[~data['Year'].isin(years_with_missing_months)]

# Extract year and month from 'CRASH DATE' and group by monthly count of incidents
data_filtered['Year_Month'] = data_filtered['CRASH DATE'].dt.to_period('M')
monthly_data = data_filtered.groupby('Year_Month').size().reset_index(name='Incident_Count')

# Save the monthly crash counts to the new directory
output_path = '/Users/avinash/Desktop/CIS/CIS607/Unit6/Final Project Preliminary Results/monthly_crash_counts_filtered.csv'
monthly_data.to_csv(output_path, index=False)
print(f"Monthly crash count data (with missing months removed) saved to {output_path}")

# Plot the monthly incident counts
plt.figure(figsize=(10, 6))
plt.plot(monthly_data['Year_Month'].astype(str), monthly_data['Incident_Count'], marker='o')
plt.title('Monthly Motor Vehicle Crash Incidents in NYC (Filtered)')
plt.xlabel('Month')
plt.ylabel('Incident Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
