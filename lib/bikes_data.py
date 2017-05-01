#!/usr/bin/env python3

'''
Connects to the database.
Pass SQL to read from the database
'''

import json
import os
import sys
import pymysql
import pymysql.cursors


# connect to the database
def connect_to_db():
    connection =  pymysql.connect(host='bikeandweather.cnkbtyr1hegq.us-east-1.rds.amazonaws.com',
                                 user='admin',
                                 password='Conv2017',
                                 db='BikeData')
    return connection


# get data from database -by passing in an sql query as a string
# create a json object with data retrieved
# this is the static station data for display on click of an icon in google map
def get_static_station_data(station_num):
    connection = connect_to_db()
    
    with connection.cursor() as cursor:
        # Create a new record
        sql_read_station_data = "SELECT * FROM BikeData.StationsStatic WHERE station = %s;"
        cursor.execute(sql_read_station_data, station_num)
        station_row = list(cursor.fetchone())
        

        station_json = { "station"  : station_row[0],
                    "name"  : station_row[1],
                    "address"  : station_row[2],
                    "lat"  : float(station_row[3]),
                    "lng"  : float(station_row[4]),
                    "bike_stands"  : station_row[8]}
        return json.dumps(station_json)
    

# get data from database -by passing in an sql query as a string
# create a json object with data retrieved
# this is the dynamic station data for display in table below google map
def get_dynamic_station_data(station_num, timestamp_from, timestamp_to):
    
    connection = connect_to_db()
    
    with connection.cursor() as cursor:
        # Create a new record
        sql_read_dynamic_data = "SELECT * FROM BikeData.StationsDynamic WHERE station =  %s and last_update >= %s and last_update <= %s;"
        cursor.execute(sql_read_dynamic_data, (station_num, timestamp_from, timestamp_to,))
        dynamic_rows = list(cursor.fetchall())
        
        sql_read_station_data = "SELECT * FROM BikeData.StationsStatic WHERE station = %s;"
        cursor.execute(sql_read_station_data, station_num)
        station_row = list(cursor.fetchone())
        
        dynamic_json = { "station"  : [ x[0] for x in dynamic_rows ],
                    "available_bike_stands"  : [ x[2] for x in dynamic_rows ],
                    "available_bikes"  : [ x[3] for x in dynamic_rows ],
                    "last_update"  : [ x[4] for x in dynamic_rows ],
                    "name"  : [ station_row[1] for x in dynamic_rows ],
                    "address"  : [ station_row[2] for x in dynamic_rows ],
                    "lat"  : [ float(station_row[3]) for x in dynamic_rows ],
                    "lng"  : [ float(station_row[4]) for x in dynamic_rows ],
                    "bike_stands"  : [ station_row[8] for x in dynamic_rows ]}
          
        return json.dumps(dynamic_json)
     
    

# get data from database -by passing in an sql query as a string
# create a json object with data retrieved
# this is the station dat for use in google map
def get_map_data():
    
    connection = connect_to_db()
    
    with connection.cursor() as cursor:
        # Create a new record
        sql_read_map_data = "SELECT station, address, lat, lng FROM BikeData.StationsStatic;"
        cursor.execute(sql_read_map_data)
    
        map_data = list(cursor.fetchall())
        
        map_json = { "station"  : [ x[0] for x in map_data ],
                    "address"  : [ x[1] for x in map_data ],
                    "lat"  : [float(x[2]) for x in map_data],
                    "lng"  : [float(x[3]) for x in map_data]}

        
        return json.dumps(map_json)
     
     

