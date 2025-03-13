import folium
import pandas as pd
import streamlit as st

import streamlit_folium as st_folium

# Load the CSV file
csv_file = "filmmap.csv"
data = pd.read_csv(csv_file)

# Create a map centered on a specific location
map_center = [38.79, -106.5348]  # Default to San Francisco
my_map = folium.Map(location=map_center, zoom_start=3)

# Add markers from the CSV
for index, row in data.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    name = row['name']
    gmap_url = row['gmap_url']
    
    # Create HTML content for the popup
    popup_html = f"""
    <b>{name}</b><br>
    <a href="{gmap_url}" target="_blank">View on Google Maps</a>
    """
    
    # Add marker with custom popup
    folium.Marker(
        [latitude, longitude], 
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color='orange',icon='circle')
    ).add_to(my_map)

# Streamlit app
st.title("Awesome Cameras Film Map")
st.write("Below is map of camera shops and film labs around the world.")

# Display the map in Streamlit
st_folium(my_map, width=800, height=550)
