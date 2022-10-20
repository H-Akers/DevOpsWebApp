import folium
import pandas

data = pandas.read_csv("/var/www/html/USA.csv")
lat = list(data["Latitude"])
long = list(data["Longitude"])
alt = list(data["Altitude"])
name = list(data["Name"])
icao = list(data["ICAO"])
intcheck = 'INTERNATIONAL'


def international(airport):
        if intcheck in airport:
            return 'red'
        else: 
            return 'blue'

map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

fg = folium.FeatureGroup(name="USA_Airports")
for lt,ln,na,al in zip(lat,long,name,alt):
    fg.add_child(folium.Marker(location=[lt,ln], popup= na + '\n' + str(al) + ' m MSL', icon=folium.Icon(international(na))))

map.add_child(fg)

map.save("index.html")