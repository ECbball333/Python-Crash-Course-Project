# Parsing the CSV File Headers
from pathlib import Path
import csv
from datetime import datetime

# Plotting Data in a Temperature Chart
import matplotlib.pyplot as plt

#path = Path('weather_data/sitka_weather_07-2021_simple.csv')
path = Path('weather_data/sitka_weather_2021_simple.csv') # Plotting a longer Timeframe
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

# Printing the Headers and their positions
#for index, column_header in enumerate(header_row):
#    print(index, column_header)

# Extracting and Reading Data
#Extract High Temps and Dates
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)
#print(highs)

# Plot the High Temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs,  color='red')

# Format plot
ax.set_title('Daily High Temperatures, 2021', fontsize=14)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()