import pandas as pd

# Load the cleaned data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned.csv'
car_data_cleaned = pd.read_csv(file_path)

# Filter the data to include only the years 2007-2017
filtered_data = car_data_cleaned[(car_data_cleaned['Year'] >= 2007) & (car_data_cleaned['Year'] <= 2017)]

# Group by Year and calculate the mean MSRP for each year
msrp_trends = filtered_data.groupby('Year')['MSRP'].mean()

# Print the MSRP trends by year
print("MSRP Trends from 2007 to 2017:\n")
print(msrp_trends)
