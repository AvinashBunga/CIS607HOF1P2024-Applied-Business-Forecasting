import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# Load the final dataset for analysis
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned_2007_2017.csv'
car_data_filtered = pd.read_csv(file_path)

# Set the style and context for the plot
sns.set(style="whitegrid", context="talk")

# Create a box plot for MSRP by Vehicle Size
plt.figure(figsize=(12, 8))
sns.boxplot(x='Vehicle Size', y='MSRP', data=car_data_filtered, palette="coolwarm")

# Customize the plot
plt.title('Box Plot of MSRP by Vehicle Size (2007-2017)', fontsize=18, weight='bold')
plt.xlabel('Vehicle Size', fontsize=14, weight='bold')
plt.ylabel('MSRP (Log Scale)', fontsize=14, weight='bold')

# Format the y-axis to show dollar values in a readable format
plt.yscale('log')  # Log scale for better visualization of the spread
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${int(x):,}'))

# Customize ticks for better readability
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Save the plot to the same directory
output_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/box_plot_msrp_vehicle_size.png'
plt.savefig(output_path, bbox_inches='tight', dpi=300)

# Show the plot
plt.show()

print(f"Box plot saved to: {output_path}")
