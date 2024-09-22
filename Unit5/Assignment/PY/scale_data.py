# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the training and testing datasets
train_data_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Train.csv"
test_data_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Test.csv"

train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

# Display the first few rows to ensure data is loaded correctly
print("First few rows of the training data:")
print(train_data.head())

print("\nFirst few rows of the testing data:")
print(test_data.head())

# Step 1: Select the relevant features for scaling
X_train = train_data[['Open', 'High', 'Low', 'Close']]
X_test = test_data[['Open', 'High', 'Low', 'Close']]

# Step 2: Initialize the scaler
scaler = StandardScaler()

# Step 3: Fit the scaler on the training data and transform both training and testing data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Convert the scaled data back to DataFrames
scaled_train_data = pd.DataFrame(X_train_scaled, columns=['Open', 'High', 'Low', 'Close'])
scaled_test_data = pd.DataFrame(X_test_scaled, columns=['Open', 'High', 'Low', 'Close'])

# Optional: Add back the Date column if needed for reference
scaled_train_data['Date'] = train_data['Date'].values
scaled_test_data['Date'] = test_data['Date'].values

# Display the first few rows of the scaled data
print("\nFirst few rows of the scaled training data:")
print(scaled_train_data.head())

print("\nFirst few rows of the scaled testing data:")
print(scaled_test_data.head())

# Step 5: Save the scaled datasets
scaled_train_data_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Train_Scaled.csv"
scaled_test_data_path = "/Users/avinash/Desktop/CIS/CIS607/Unit5/Assignment/USDINRX_Test_Scaled.csv"

scaled_train_data.to_csv(scaled_train_data_path, index=False)
scaled_test_data.to_csv(scaled_test_data_path, index=False)

print(f"\nScaled training data saved as: {scaled_train_data_path}")
print(f"Scaled testing data saved as: {scaled_test_data_path}")
