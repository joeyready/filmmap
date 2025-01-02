import pandas as pandas
import folium

# csv_to_sqlite('filmmap.csv', 'filmmap.db', 'filmmap')

# Create a map centered on a specific location
map_center = [37.7749, -122.4194] # San Francisco
my_map = folium.Map(location=map_center, zoom_start=12)

# Add a marker
folium.Marker([37.7749, -122.4194], popup="San Francisco").add_to(my_map)

# Save the map as an HTML file
my_map.save("my_map.html")