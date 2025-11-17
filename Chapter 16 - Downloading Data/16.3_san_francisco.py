from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/san_francisco_data.csv')
lines = path.read_text(encoding='utf8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[11])
        low = int(row[12])
    except ValueError:
        print(f'Data not available for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#print(highs)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = 'San Francisco Highs and Lows'
ax.set_title(title)
ax.set_xlabel('Date', fontsize=20)
ax.set_ylabel('Temps', fontsize=20)
fig.autofmt_xdate()
ax.tick_params(labelsize=20)

plt.show()






