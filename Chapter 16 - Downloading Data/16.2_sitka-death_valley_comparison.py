
# Parsing the CSV File Headers
from pathlib import Path
import csv
from datetime import datetime

# Plotting Data in a Temperature Chart
import matplotlib.pyplot as plt

#path = Path('weather_data/sitka_weather_07-2021_simple.csv')
path = Path('weather_data/death_valley_2021_simple.csv') # Plotting a longer Timeframe
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

# Printing the Headers and their positions
#for index, column_header in enumerate(header_row):
#    print(index, column_header)

# Extracting and Reading Data
#Extract High Temps, Low Temps, and Dates
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try: # Added Error Handling
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
#print(highs)

# Plot the High and Low Temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs,  color='red', alpha=0.5) # Added alpha value to control transparency
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Added Shading to the chart

# Format plot
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()