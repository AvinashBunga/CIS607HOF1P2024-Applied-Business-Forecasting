import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
data_path = '/Users/avinash/Desktop/CIS/CIS607/Unit6/Final Project Preliminary Results/monthly_crash_counts_filtered.csv'
data = pd.read_csv(data_path)

# Convert 'Year_Month' to datetime format
data['Year_Month'] = pd.to_datetime(data['Year_Month'], format='%Y-%m')

# Extract the month for further analysis
data['Month'] = data['Year_Month'].dt.month

# Define winter (Nov-Feb) and summer (Jun-Aug) months
winter_months = [11, 12, 1, 2]
summer_months = [6, 7, 8]

# Filter for winter and summer months
winter_data = data[data['Month'].isin(winter_months)]
summer_data = data[data['Month'].isin(summer_months)]

# Calculate average incidents for winter and summer months
avg_winter_incidents = winter_data['Incident_Count'].mean()
avg_summer_incidents = summer_data['Incident_Count'].mean()

# Print results for Hypothesis 1
print(f"Average incidents in Winter months (Nov-Feb): {avg_winter_incidents}")
print(f"Average incidents in Summer months (Jun-Aug): {avg_summer_incidents}")

# Create the output directory if it doesn't exist
output_dir = '/Users/avinash/Desktop/CIS/CIS607/Unit6/Hypothesis 1'
os.makedirs(output_dir, exist_ok=True)

# Save results to a CSV file
output_csv_path = os.path.join(output_dir, 'hypothesis_1_results.csv')
result_data = pd.DataFrame({
    'Season': ['Winter (Nov-Feb)', 'Summer (Jun-Aug)'],
    'Average Incident Count': [avg_winter_incidents, avg_summer_incidents]
})
result_data.to_csv(output_csv_path, index=False)

# Bar chart for Hypothesis 1 (Winter vs Summer comparison)
plt.figure(figsize=(8, 5))
plt.bar(['Winter (Nov-Feb)', 'Summer (Jun-Aug)'], [avg_winter_incidents, avg_summer_incidents], color=['blue', 'orange'])
plt.title('Average Motor Vehicle Incidents: Winter vs Summer')
plt.ylabel('Average Incident Count')

# Save the plot to the directory
plot_path = os.path.join(output_dir, 'winter_vs_summer_incidents.png')
plt.tight_layout()
plt.savefig(plot_path)
plt.show()

print(f"Results and plot saved to {output_dir}")
