
'''
I used this file to test parts of my code as I was 
developing this app.
'''



import time
import datetime
import lib.bikes_data as bikes_data

# test_data = bikes_data.get_static_station_data(30)
# 
#  map_data = bikes_data.get_map_data()
# 
# dynamic_data = bikes_data.get_dynamic_station_data(102, 1491657347, 1491659947)
# 
# print(dynamic_data)

num = 43200 + 1491692400 + 3599
print(num)


print(
    datetime.datetime.fromtimestamp(
        int("1491735600")
    ).strftime('%Y-%m-%d %H:%M:%S')
)


a_date = "15/04/2017"
a_timestamp = time.mktime(datetime.datetime.strptime(a_date, "%d/%m/%Y").timetuple())
print(int(a_timestamp))







