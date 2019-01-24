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

#map layer
map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")

#creating feature group (1 layer)
fg_volcanos = folium.FeatureGroup(name="My Map")

#iterating
for lt, ln, el in zip(lat, lon, elev):
    fg_volcanos.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=str(el)+" m",
    fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))

#creating feature group (2 layer)
fg_population = folium.FeatureGroup(name="Population")

#feature child which is responsible for country borders(poligons) (2 layer)
fg_population.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
            style_function=lambda x: {"fillColor":"orange" if x["properties"]["POP2005"] < 10000000
            else "blue" if 10000000 <= x["properties"]["POP2005"] < 200000000 else "red"}))


#assigning fg to map, add two layers to the map
map.add_child(fg_volcanos)
map.add_child(fg_population)

#adding layer control (must be added after assigning map adding feature group
map.add_child(folium.LayerControl(position="topright", collapsed=True, autoZIndex=True))

#saving data to the file
map.save("Map1.html")