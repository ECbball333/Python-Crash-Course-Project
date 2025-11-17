from pathlib import Path
import json
import plotly.express as px

# Load GeoJSON earthquake data
data_path = Path('eq_data/eq_data_30_day_m1.geojson')
eq_data = json.loads(data_path.read_text(encoding='utf-8'))

# Optional: Save a pretty-printed version of the data
readable_path = Path('eq_data/readable_eq_data.geojson')
readable_path.write_text(json.dumps(eq_data, indent=4))

# Extract dataset title from metadata
title = eq_data['metadata']['title']

# Extract earthquake data entries
all_eq_dicts = eq_data['features']

# Extract magnitude, longitude, latitude, and title in a single pass
mags, lons, lats, titles = map(list, zip(*[
    (
        eq['properties']['mag'],
        eq['geometry']['coordinates'][0],
        eq['geometry']['coordinates'][1],
        eq['properties']['title']
    )
    for eq in all_eq_dicts
]))

# Build and show the world map
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth',
    hover_name=titles,
    title=title  # Title from metadata
)

fig.show()
