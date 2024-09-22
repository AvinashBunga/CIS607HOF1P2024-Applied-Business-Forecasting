import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
data_path = '/Users/avinash/Desktop/CIS/CIS607/Unit6/Final Project Preliminary Results/monthly_crash_counts_filtered.csv'
data = pd.read_csv(data_path)

# Convert 'Year_Month' to datetime format
data['Year_Month'] = pd.to_datetime(data['Year_Month'], format='%Y-%m')

# Extract the year for further analysis
data['Year'] = data['Year_Month'].dt.year

# Group by year and calculate the total number of incidents per year
annual_trend = data.groupby('Year')['Incident_Count'].sum().reset_index()

# Calculate the average number of incidents before 2020 (2013-2019)
avg_pre_2020_incidents = annual_trend[annual_trend['Year'] < 2020]['Incident_Count'].mean()

# Get the total incidents for 2020
incidents_2020 = annual_trend[annual_trend['Year'] == 2020]['Incident_Count'].values[0]

# Create the output directory if it doesn't exist
output_dir = '/Users/avinash/Desktop/CIS/CIS607/Unit6/Hypothesis 3'
os.makedirs(output_dir, exist_ok=True)

# Save the results to a CSV file
output_csv_path = os.path.join(output_dir, 'hypothesis_3_comparison.csv')
result_data = pd.DataFrame({
    'Year': ['Pre-2020 Average', '2020'],
    'Incident Count': [avg_pre_2020_incidents, incidents_2020]
})
result_data.to_csv(output_csv_path, index=False)

# Plot the comparison between pre-2020 average and 2020 incidents
plt.figure(figsize=(8, 5))
plt.bar(['Pre-2020 Average', '2020'], [avg_pre_2020_incidents, incidents_2020], color=['blue', 'orange'])
plt.title('Comparison of Crash Incidents: Pre-2020 Average vs 2020')
plt.ylabel('Incident Count')

# Save the plot to the directory
plot_path = os.path.join(output_dir, 'pre_2020_vs_2020_incidents.png')
plt.tight_layout()
plt.savefig(plot_path)
plt.show()

print(f"Results and plot saved to {output_dir}")
