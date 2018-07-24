#! /usr/bin/python3.5

import sqlite3
import pandas as pd

db = sqlite3.connect('hubway.db')

def run_query(query):
    return pd.read_sql_query(query, db)


# SELECT: returns all rows showing start_date and bike_number, which is too many
query = 'SELECT start_date, bike_number FROM trips;' 

# * wildcard keyword: see all columns up to five rows
query = 'SELECT * FROM trips LIMIT 5;'

# LIMIT: see duration and start_date columns up to ten rows
query = 'SELECT duration, start_date FROM trips LIMIT 10;'

# ORDER BY: order by a certain column using ORDER BY column ASC/DESC (asc is default)
query = '''
SELECT duration
FROM trips 
ORDER BY duration DESC 
LIMIT 25;
'''

# WHERE keyword
query = '''
SELECT *
FROM trips
WHERE duration > 9990
ORDER BY duration DESC;
'''

# AND/OR keyword 
query = '''
SELECT * 
FROM trips
WHERE duration > 9800 
    AND sub_type == "Registered"
ORDER BY duration DESC;
'''

# COUNT(*) will return the number of rows found
query ='''
SELECT COUNT(*)
FROM trips
WHERE sub_type == "Registered";
'''

# AS will change the column title
query = '''
SELECT COUNT(*) AS "Total Trips by Registered"
FROM trips
WHERE sub_type == "Registered";
'''

# SUM, MAX, MIN, AVG
query = '''
SELECT AVG(duration) AS "Average trip duration"
FROM trips
WHERE sub_type == "Registered";
'''

# GROUP BY
query = '''
SELECT sub_type, AVG(duration) AS "Average trip duration"
FROM trips
GROUP BY sub_type;
'''

# Which bike was used for the most number of trips?
query = '''
SELECT bike_number AS "Bike Number", 
       COUNT(*) AS "Number of Trips on This Bike"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(*) DESC
LIMIT 1;
'''

# Average duration of users over 30
query = '''
SELECT AVG(duration) AS "Average trip length of users over 30"
FROM trips
WHERE (2017 - birth_date) > 30;
'''

# INNER JOIN ... ON 
query = '''
SELECT trips.start_station, stations.station, COUNT(*) AS "Total Number Of Trips From Starting Point"
FROM trips
INNER JOIN stations
ON trips.start_station= stations.id
GROUP BY trips.start_station
ORDER BY COUNT(*) DESC
LIMIT 20;
'''

# Which stations are most used for round trips?
query = '''
SELECT stations.station,
       COUNT(*) AS "Total Round Trips From This Station"
FROM trips
INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station == trips.end_station
GROUP BY trips.start_station
ORDER BY COUNT(*) DESC
limit 20;
'''

# TWO JOINS: How many trips start and end on different municipalities?
query = '''
SELECT COUNT(*) AS "Total Trips Across Municipalities"
FROM trips
INNER JOIN stations AS start
ON trips.start_station = start.id
INNER JOIN stations AS endstation
ON trips.end_station = endstation.id
WHERE start.municipality != endstation.municipality 
ORDER BY COUNT(*) DESC
limit 10
'''

# How many trips occurred additioanl fees? (Over 30 minutes, which is 1800 seconds)
query = '''
SELECT COUNT(*) AS "Total Trips Over 30 Minutes"
FROM trips
WHERE duration > 1800
ORDER BY COUNT(*) DESC;
'''

# Which bike was used for the most minutes?
query = '''
SELECT bike_number, SUM(duration) AS "Total Minutes On Bike"
FROM trips
GROUP BY bike_number
ORDER BY SUM(duration) DESC
LIMIT 5;
'''
# Did registered or casual users make more round trips?
query = '''
SELECT sub_type, COUNT(*) AS "Round Trips Made"
FROM trips
WHERE start_station == end_station
GROUP BY sub_type;
'''

# Which municipality had the longest average duration?
query = '''
SELECT stations.municipality, AVG(trips.duration) AS "Average Duration"
FROM trips
INNER JOIN stations
ON trips.start_station = stations.id
GROUP BY stations.municipality
ORDER BY AVG(trips.duration) DESC
LIMIT 10;
'''
print(run_query(query))