import pandas as pd

# Define the path to your dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit3/Trending videos on youtube dataset.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Initial DataFrame Info:")
print(df.info())

# Check for missing values in each column
missing_values = df.isna().sum()

# Create a DataFrame to display column names and their missing value counts
missing_values_df = pd.DataFrame(missing_values, columns=['Missing Values'])
missing_values_df = missing_values_df[missing_values_df['Missing Values'] > 0]  # Filter only columns with missing values

print("\nColumns with Missing Values and Their Counts:")
print(missing_values_df)

# Save the missing data report to a CSV for further review if needed
missing_data_report_path = '/Users/avinash/Desktop/CIS/CIS607/Unit3/Missing_Data_Report.csv'
missing_values_df.to_csv(missing_data_report_path, header=True)
print("\nMissing data report saved to:", missing_data_report_path)
