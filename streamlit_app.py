import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Water Quality Explorer")

# Upload files
st.sidebar.header("Upload Files")
station_file = st.sidebar.file_uploader("Upload station.csv", type="csv")
results_file = st.sidebar.file_uploader("Upload narrowresult.csv", type="csv")

if station_file and results_file:
    # Load data
    station_df = pd.read_csv(station_file)
    results_df = pd.read_csv(results_file)

    # Clean data
    results_df['ResultMeasureValue'] = pd.to_numeric(results_df['ResultMeasureValue'], errors='coerce')
    results_df['ActivityStartDate'] = pd.to_datetime(results_df['ActivityStartDate'], errors='coerce')
    valid_df = results_df.dropna(subset=["ResultMeasureValue", "ActivityStartDate", "CharacteristicName"])

    # Generate dummy coordinates for mapping (real lat/lon not provided)
    stations = station_df[['MonitoringLocationIdentifier', 'MonitoringLocationName']].drop_duplicates()
    np.random.seed(42)
    stations['Latitude'] = np.random.uniform(36.5, 39.0, len(stations))
    stations['Longitude'] = np.random.uniform(-89.5, -84.5, len(stations))

    # Sidebar filters
    st.sidebar.header("Filter Data")
    contaminants = sorted(valid_df['CharacteristicName'].dropna().unique())
    selected_contaminant = st.sidebar.selectbox("Select a contaminant:", contaminants)

    subset = valid_df[valid_df["CharacteristicName"] == selected_contaminant]

    # Date and value sliders
    date_min = subset["ActivityStartDate"].min()
    date_max = subset["ActivityStartDate"].max()
    value_min = float(subset["ResultMeasureValue"].min())
    value_max = float(subset["ResultMeasureValue"].max())

    selected_date_range = st.sidebar.date_input("Date Range", [date_min, date_max])
    selected_value_range = st.sidebar.slider("Value Range", value_min, value_max, (value_min, value_max))

    # Filter data
    filtered = subset[
        (subset["ActivityStartDate"] >= pd.to_datetime(selected_date_range[0])) &
        (subset["ActivityStartDate"] <= pd.to_datetime(selected_date_range[1])) &
        (subset["ResultMeasureValue"].between(selected_value_range[0], selected_value_range[1]))
    ]

    st.markdown("### Matching Stations Map")
    matching_stations = filtered['MonitoringLocationIdentifier'].unique()
    mapped_stations = stations[stations['MonitoringLocationIdentifier'].isin(matching_stations)]

    # Map
    m = folium.Map(location=[37.5, -86], zoom_start=7)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in mapped_stations.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['MonitoringLocationName']
        ).add_to(marker_cluster)

    st_data = st_folium(m, width=700, height=500)

    # Trend plot
    st.markdown("### Contaminant Trend Over Time")
    fig, ax = plt.subplots(figsize=(12, 6))
    for station_id, group in filtered.groupby("MonitoringLocationIdentifier"):
        ax.plot(group["ActivityStartDate"], group["ResultMeasureValue"], label=station_id)
    ax.set_title(f"{selected_contaminant} Levels Over Time")
    ax
