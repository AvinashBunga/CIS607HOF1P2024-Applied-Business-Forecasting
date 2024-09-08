import pandas as pd

# File path to the cleaned dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Cleaned_Motor_Vehicle_Collisions.csv'

# Load the cleaned dataset
data = pd.read_csv(file_path)

# Ensure CRASH DATE is in datetime format
data['CRASH DATE'] = pd.to_datetime(data['CRASH DATE'], errors='coerce')

# Extract Year and Month from the CRASH DATE column
data['YEAR'] = data['CRASH DATE'].dt.year
data['MONTH'] = data['CRASH DATE'].dt.month

# Group by Year and Month to get the count of records
yearly_counts = data['YEAR'].value_counts().sort_index()
monthly_counts = data.groupby(['YEAR', 'MONTH']).size().reset_index(name='COUNT')

# Display yearly counts
print("Count of Records for Each Year:")
print(yearly_counts)

# Display monthly counts
print("\nCount of Records for Each Year and Month:")
print(monthly_counts)

# Optional: Save the counts to a CSV file for further analysis
monthly_counts.to_csv('/Users/avinash/Desktop/CIS/CIS607/Unit4/Project/Year_Month_Counts.csv', index=False)
