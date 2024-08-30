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

# Display columns with missing values for reference
print("\nColumns with Missing Values and Their Counts:")
print(missing_values[missing_values > 0])

# Drop rows with any missing values
df.dropna(inplace=True)

# Display information after dropping missing values
print("\nDataFrame Info After Dropping Missing Values:")
print(df.info())

# Ensure numeric columns are of the correct data type (optional but good practice)
numeric_columns = ['durationSec', 'viewCount', 'likeCount', 'dislikeCount', 'commentCount']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Save the cleaned dataset
cleaned_file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit3/Cleaned_Trending_videos_on_youtube_dataset.csv'
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning completed. Cleaned data saved to:", cleaned_file_path)
