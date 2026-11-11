import pandas as pd
import matplotlib.pyplot as plt

#Skip the descriptive lines and read the data into a pandas DataFrame
cpi_data = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)

#Convert date column into datetime format
cpi_data['date'] = pd.to_datetime(cpi_data['date'])
#Calculate annual percentage change
cpi_data['Annual Change'] = cpi_data['STATIC_INFLATIONCALC'].pct_change(periods=12) * 100

#Create the figure
fig, ax1 = plt.subplots(figsize=(14, 8), layout='constrained')
#Plot CPI
ax1.plot(cpi_data['date'], cpi_data['STATIC_INFLATIONCALC'], label='CPI')
# Create second Y-axis for annual percentage change
ax2 = ax1.twinx()

#Plot annual percentage change
ax2.plot(cpi_data['date'], cpi_data['Annual Change'], label='Annual Percentage Change', color='orange')

#Add dotted base level 
ax1.axhline(y=100, linestyle=':', color='red', label='Base Level (100)')

#Setup axis labels and title
ax1.set_xlabel('Year')
ax1.set_ylabel('Consumer Price Index (CPI)')
ax2.set_ylabel('Annual Percentage Change (%)')
ax1.set_title('Canadian CPI and Annual Inflation Rate', fontsize=16)

#Combine legends for both lines 
cpi_lines, cpi_labels = ax1.get_legend_handles_labels()
percentage_lines, percentage_labels = ax2.get_legend_handles_labels()

#Display legend with its corresponding lines and at the lower right locaiton for visibility
ax1.legend(cpi_lines + percentage_lines, cpi_labels + percentage_labels, loc='lower right')

#Save and display graph with DPI 300
savefig_path = "CPI_Graph.png"
plt.savefig(savefig_path, dpi = 300)
plt.show()

