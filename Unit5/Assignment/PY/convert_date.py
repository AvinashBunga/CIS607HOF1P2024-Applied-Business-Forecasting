# Import necessary libraries
import pandas as pd

# Load your cleaned data file
file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Cleaned.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset before date conversion:")
print(data.head())

# Check the current data type of the 'Date' column
print("\nData types before conversion:")
print(data.dtypes)

# Step 1: Convert the 'Date' column to datetime format
# Use 'errors="coerce"' to handle any non-standard date formats
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Step 2: Check for any potential issues after conversion
# Display any rows where the 'Date' conversion resulted in NaT (Not a Time)
conversion_issues = data[data['Date'].isna()]
if not conversion_issues.empty:
    print("\nRows with conversion issues (Date could not be converted):")
    print(conversion_issues)
else:
    print("\nDate conversion successful. No conversion issues detected.")

# Display the first few rows and data types after conversion to confirm the changes
print("\nFirst few rows of the dataset after date conversion:")
print(data.head())

print("\nData types after conversion:")
print(data.dtypes)

# Step 3: Save the updated dataset with the converted 'Date' column
# Save the modified data to a new file
updated_file_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Cleaned_Updated.csv"
data.to_csv(updated_file_path, index=False)
print(f"\nUpdated dataset saved as '{updated_file_path}'.")
