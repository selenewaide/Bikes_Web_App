
import lib.bikes_data as bikes_data

#test_data = bikes_data.get_static_station_data(30)

map_data = bikes_data.get_map_data()
print(map_data[0])
print(type(map_data))
#print(map_data[0])