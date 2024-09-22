import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
import numpy as np

# Load the final dataset for analysis
file_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/Car_Features_and_MSRP_Cleaned_2007_2017.csv'
car_data_filtered = pd.read_csv(file_path)

# Set the style and context for the plot
sns.set(style="whitegrid", context="talk")

# Create a color palette with a temperature range
palette = sns.color_palette("coolwarm", as_cmap=True)

# Create a histogram for MSRP with the color palette and log scale on X-axis
plt.figure(figsize=(12, 8))
hist = sns.histplot(car_data_filtered['MSRP'], bins=np.logspace(np.log10(10000), np.log10(2000000), 30), kde=False, edgecolor='black')

# Annotate each bar with the count value
for p in hist.patches:
    height = p.get_height()
    if height > 0:  # Only annotate bars with counts greater than 0
        hist.annotate(f'{int(height)}', xy=(p.get_x() + p.get_width() / 2, height), 
                      xytext=(0, 5), textcoords='offset points', ha='center', fontsize=10, color='black')

# Customize the plot
plt.title('Histogram of MSRP (2007-2017)', fontsize=18, weight='bold')
plt.xlabel('MSRP ($)', fontsize=14, weight='bold')
plt.ylabel('Number of Vehicles', fontsize=14, weight='bold')

# Apply a logarithmic scale to the X-axis
plt.xscale('log')

# Format the X-axis to show specific dollar values at log scale
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${int(x):,}'))

# Add more specific tick marks for readability, including the highest value
plt.gca().set_xticks([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000, 200000, 300000, 500000, 1000000, 2000000])

# Apply the color gradient to the bars
for i, patch in enumerate(hist.patches):
    patch.set_facecolor(palette(i / len(hist.patches)))

# Add a color bar legend with $ values and reduce its size for better readability
sm = plt.cm.ScalarMappable(cmap=palette, norm=plt.Normalize(vmin=car_data_filtered['MSRP'].min(), vmax=car_data_filtered['MSRP'].max()))
sm.set_array([])
cbar = plt.colorbar(sm, ax=hist.axes, orientation='horizontal', pad=0.2)
cbar.set_label('MSRP ($)', fontsize=12)
cbar.set_ticks([10000, 500000, 1000000, 2000000])
cbar.ax.set_xticklabels(['$10,000', '$500,000', '$1,000,000', '$2,000,000'], fontsize=10)

# Customize ticks for better readability
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Save the histogram to the same directory
output_path = '/Users/avinash/Desktop/CIS/CIS 607/Unit 1/U1 Assignment/histogram_msrp_final_detailed.png'
plt.savefig(output_path, bbox_inches='tight', dpi=300)

# Show the plot
plt.show()

print(f"Histogram saved to: {output_path}")
