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

# use pandas to create a dataframe
df = pd.read_sql_query(r'SELECT * FROM airlines LIMIT 15 ;', db)
print(df['name'])

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

# # fetchall returns a list of tuples
# coords = cur.execute(query).fetchall()

# x, y = m(
#     [l[0] for l in coords],
#     [l[1] for l in coords]
# )

# m.scatter(x, y, 1, marker='o', color='red')

routes = pd.read_sql_query('''
        SELECT cast (source_airports.longitude as float) as source_lon,
        cast (source_airports.latitude as float) as source_lat,
        cast (dest_airports.longitude as float) as dest_lon,
        cast (dest_airports.latitude as float) as dest_lat
        FROM routes
        INNER JOIN airports source_airports ON
        source_airports.id = routes.source_id
        INNER JOIN airports dest_airports ON
        dest_airports.id = routes.dest_id;
        ''', db)

for name, row in routes[:3000].iterrows():
    if abs(row["source_lon"] - row["dest_lon"]) < 90:
        # draw a great circle between source and dest airports
        m.drawgreatcircle(
            row["source_lon"],
            row["source_lat"],
            row["dest_lon"],
            row["dest_lat"],
            linewidth = 1,
            color='b'
        )

plt.show()

# close cursor object and database
cur.close()
db.close()
