#! /usr/bin/python3.5

# airports : id, name, city, country, code, icao, lat, lon, offset, dst, timezone
# airlines : id, name, alias, iata, icao, callsign, country, active
# routes : airline, airline_id, source, source_id, dest, dest_id, codeshare, stops, equipment

import sqlite3
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# connect to data base and create cursor object
db = sqlite3.connect('flights.db')
cur = db.cursor() # cursor object that can execute and fetchall results

m = Basemap(
    projection='merc',
    llcrnrlat=-80,
    urcrnrlat=80,
    llcrnrlon=-180,
    urcrnrlon=180,
    lat_ts=20,
    resolution='c'
)

m.drawcoastlines()
m.drawmapboundary()

query = r'''
SELECT cast(longitude as float),
cast(latitude as float)
from airports;
'''

# fetchall returns a list of tuples
coords = cur.execute(query).fetchall()

x, y = m(
    [l[0] for l in coords],
    [l[1] for l in coords]
)

m.scatter(x, y, 1, marker='o', color='red')

plt.show()

# close cursor object and database
cur.close()
db.close()
