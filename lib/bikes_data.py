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


def connect_to_db():
    # Connect to the database
    connection =  pymysql.connect(host='bikeandweather.cnkbtyr1hegq.us-east-1.rds.amazonaws.com',
                                 user='admin',
                                 password='Conv2017',
                                 db='BikeData')
    return connection


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
    
def get_map_data():
    
    connection = connect_to_db()
    
    with connection.cursor() as cursor:
        # Create a new record
        sql_read_map_data = "SELECT station, lat, lng FROM BikeData.StationsStatic;"
        cursor.execute(sql_read_map_data)
    
        map_data = list(cursor.fetchall())
        
        map_json = { "station"  : [ x[0] for x in map_data ],
                    "lat"  : [float(x[1]) for x in map_data],
                    "lng"  : [float(x[2]) for x in map_data]}

        
        return json.dumps(map_json)
     
     

