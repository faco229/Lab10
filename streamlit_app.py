import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import numpy as np

st.title("Water Quality Analysis App")

# Auto-load CSV files from local repo (same folder as streamlit_app.py)
station_df = pd.read_csv("station.csv")
results_df = pd.read_csv("narrowresult.csv")

# Filter unique stations
stations = station_df[['MonitoringLocationIdentifier', 'MonitoringLocationName']].drop_duplicates()

# Generate dummy lat/lon for stations
np.random.seed(42)
stations['Latitude'] = np.random.uniform(36.5, 39.0, len(stations))
stations['Longitude'] = np.random.uniform(-89.5, -84.5, len(stations))

# Convert ResultMeasureValue to numeric early
results_df['ResultMeasureValue'] = pd.to_numeric(results_df['ResultMeasureValue'], errors='coerce')

# Contaminant selection
contaminants = results_df['CharacteristicName'].dropna().unique()
selected_contaminants = st.multiselect("Select up to 2 contaminants:", options=sorted(contaminants), max_selections=2)

# Filter by date range
results_df['ActivityStartDate'] = pd.to_datetime(results_df['ActivityStartDate'], errors='coerce')
min_date = results_df['ActivityStartDate'].min()
max_date = results_df['ActivityStartDate'].max()
date_range = st.date_input("Select date range:", [min_date, max_date])

# Value range filter (only use numeric values)
if not valid_results_df['ResultMeasureValue'].dropna().empty:
    value_min = float(valid_results_df['ResultMeasureValue'].min())
    value_max = float(valid_results_df['ResultMeasureValue'].max())
else:
    value_min = 0.0
    value_max = 100.0  # fallback default


# Filter data
filtered = results_df[
    results_df['CharacteristicName'].isin(selected_contaminants) &
    (results_df['ActivityStartDate'] >= pd.to_datetime(date_range[0])) &
    (results_df['ActivityStartDate'] <= pd.to_datetime(date_range[1])) &
    (results_df['ResultMeasureValue'].between(value_range[0], value_range[1]))
].dropna(subset=['ResultMeasureValue'])

# Map
st.subheader("Map of Selected Stations")
matching_stations = filtered['MonitoringLocationIdentifier'].unique()
mapped_stations = stations[stations['MonitoringLocationIdentifier'].isin(matching_stations)]

map_center = [37.5, -86.0]
m = folium.Map(location=map_center, zoom_start=7)
marker_cluster = MarkerCluster().add_to(m)

for _, row in mapped_stations.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['MonitoringLocationName']
    ).add_to(marker_cluster)

st_data = st_folium(m, width=700, height=500)

# Trend Plot
st.subheader("Trend Plot")
fig, ax = plt.subplots(figsize=(10, 5 * len(selected_contaminants)))

if len(selected_contaminants) == 1:
    data = filtered[filtered['CharacteristicName'] == selected_contaminants[0]]
    for station_id, group in data.groupby('MonitoringLocationIdentifier'):
        ax.plot(group['ActivityStartDate'], group['ResultMeasureValue'], label=station_id)
    ax.set_title(f"{selected_contaminants[0]} Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Measured Value")
    ax.legend(fontsize='small')
    ax.grid(True)
    st.pyplot(fig)

elif len(selected_contaminants) == 2:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    for i, ax in enumerate([ax1, ax2]):
        data = filtered[filtered['CharacteristicName'] == selected_contaminants[i]]
        for station_id, group in data.groupby('MonitoringLocationIdentifier'):
            ax.plot(group['ActivityStartDate'], group['ResultMeasureValue'], label=station_id)
        ax.set_title(f"{selected_contaminants[i]} Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Measured Value")
        ax.legend(fontsize='x-small')
        ax.grid(True)
    st.pyplot(fig)
