import folium
import pandas

#adding data from file
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#conditionals about elevation
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'blue'

#map layer (first layer)
map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")

#creating feature group (2 layer)
fg = folium.FeatureGroup(name="My Map")
#iterating
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=str(el)+" m",
    fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))


#assigning fg to map
map.add_child(fg)
#saving data to the file
map.save("Map1.html")