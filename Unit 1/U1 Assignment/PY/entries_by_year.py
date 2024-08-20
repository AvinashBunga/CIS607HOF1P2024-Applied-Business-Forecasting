import pandas as pd

# Load the cleaned data
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned.csv'
car_data_cleaned = pd.read_csv(file_path)

# Step 1: Group the data by Year and count the number of entries for each year
entries_by_year = car_data_cleaned['Year'].value_counts().sort_index()

# Print the number of entries for each year
print("Number of entries by year:\n")
print(entries_by_year)
