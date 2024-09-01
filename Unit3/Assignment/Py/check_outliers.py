# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file path
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit3/Assignment/Selective_Encoded_Dataset.csv"

# Load the dataset
data = pd.read_csv(file_path)

# List of numerical columns to check for outliers
numerical_columns = ['duration', 'days_left', 'price']

# Display basic statistics to understand the spread of data
print("Summary statistics of numerical columns:")
print(data[numerical_columns].describe())

# Plotting box plots to visually identify outliers
plt.figure(figsize=(15, 5))

for i, col in enumerate(numerical_columns):
    plt.subplot(1, 3, i + 1)
    sns.boxplot(y=data[col])
    plt.title(f"Boxplot of {col}")

plt.tight_layout()
plt.show()
