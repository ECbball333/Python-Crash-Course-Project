from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

dates, prec = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prec.append(int(row[4]))
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 5))
#ax.plot(dates, prec, color='red')
ax.bar(dates, prec, width=1.0, align="center", color="tab:blue")

ax.set_title("Sitka Precipitation Data - 2021")
ax.set_xlabel('Date')
ax.set_ylabel('Precipitation [inches]')
fig.autofmt_xdate()
ax.grid(True, axis="y", linewidth=0.4, alpha=0.4)

plt.tight_layout()
plt.show()








