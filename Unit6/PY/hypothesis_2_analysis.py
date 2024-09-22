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

# Create the output directory if it doesn't exist
output_dir = '/Users/avinash/Desktop/CIS/CIS607/Unit6/Hypothesis 2'
os.makedirs(output_dir, exist_ok=True)

# Save the results to a CSV file
output_csv_path = os.path.join(output_dir, 'hypothesis_2_annual_trend.csv')
annual_trend.to_csv(output_csv_path, index=False)

# Plot the trend over the years
plt.figure(figsize=(10, 6))
plt.plot(annual_trend['Year'], annual_trend['Incident_Count'], marker='o', color='b', label='Total Incidents')
plt.title('Yearly Trend of Motor Vehicle Crash Incidents in NYC')
plt.xlabel('Year')
plt.ylabel('Incident Count')
plt.grid(True)
plt.legend()

# Save the plot to the directory
plot_path = os.path.join(output_dir, 'annual_incidents_trend.png')
plt.tight_layout()
plt.savefig(plot_path)
plt.show()

print(f"Results and plot saved to {output_dir}")
