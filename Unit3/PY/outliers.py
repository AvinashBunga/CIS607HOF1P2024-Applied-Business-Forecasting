import pandas as pd

# Define the path to your cleaned dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit3/Cleaned_Trending_videos_on_youtube_dataset.csv'

# Load the cleaned dataset
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Initial DataFrame Info:")
print(df.info())

# Detect and remove outliers using the Interquartile Range (IQR) method for the 'viewCount' column
Q1 = df['viewCount'].quantile(0.25)
Q3 = df['viewCount'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for filtering outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers from the dataset
df_cleaned = df[(df['viewCount'] >= lower_bound) & (df['viewCount'] <= upper_bound)]

print("\nDataFrame Info After Removing Outliers:")
print(df_cleaned.info())

# Save the dataset after removing outliers
outlier_removed_file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit3/Cleaned_Trending_videos_without_outliers.csv'
df_cleaned.to_csv(outlier_removed_file_path, index=False)

print("Outliers removed. Cleaned data saved to:", outlier_removed_file_path)
