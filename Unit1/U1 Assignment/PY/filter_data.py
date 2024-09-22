import pandas as pd

# Load the cleaned data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned.csv'
car_data_cleaned = pd.read_csv(file_path)

# Filter the data to include only the years 2007-2017
filtered_data = car_data_cleaned[(car_data_cleaned['Year'] >= 2007) & (car_data_cleaned['Year'] <= 2017)]

# Save the filtered data to a new CSV file
filtered_file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned_2007_2017.csv'
filtered_data.to_csv(filtered_file_path, index=False)

print("Filtered data has been saved to:", filtered_file_path)
