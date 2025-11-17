import pandas as pd
import plotly.express as px
from pathlib import Path

# Load fire data
df = pd.read_csv('eq_data/world_fires_1_day.csv')

# Extract values directly from the DataFrame
lats = df['latitude']
lons = df['longitude']
brightness = df['brightness']
dates = df['acq_date']
confidence = df['confidence']

# Optional: filter out low-confidence fires
# df = df[df['confidence'] > 30]

# Use brightness or frp as size and color
fig = px.scatter_geo(
    df,
    lat='latitude',
    lon='longitude',
    color='brightness',  # or use 'frp' for fire intensity
    size='brightness',
    hover_name='acq_date',
    hover_data={'confidence': True, 'frp': True, 'latitude': False, 'longitude': False},
    color_continuous_scale='Hot',
    projection='natural earth',
    title='Global Fire Detections'
)

fig.show()
# Save image to PNG file
fig.write_image("global_fires_map.png", width=1200, height=700)
