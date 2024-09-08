import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load your dataset
file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Assignment/MentalHealthSurvey.csv'
data = pd.read_csv(file_path)

# Display the first few rows to confirm the data is loaded correctly
print("Dataset loaded successfully. Here are the first few rows:")
print(data.head())

# List of categorical columns to be encoded
categorical_columns = ['gender', 'university', 'degree_level', 'degree_major', 'academic_year',
                       'cgpa', 'residential_status', 'campus_discrimination', 'sports_engagement',
                       'average_sleep', 'stress_relief_activities']

# Applying label encoding to categorical columns
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Scaling the numeric columns
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# Saving the cleaned and prepared dataset for R analysis
cleaned_file_path = '/Users/avinash/Desktop/CIS/CIS607/Unit4/Assignment/MentalHealthSurvey_Cleaned.csv'
data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")
