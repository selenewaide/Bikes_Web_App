From: Selene Waide
Project: Dublin Bikes Web App
Position Applied for: 
Date: 1 May 2017

1. Link to repo:

2. About the code:
This application has been written by me. It is a full stack solution.

3. Technologies leveraged:
a) Amazon EC2 instance - getting data from jcdecaux.com API.
b) Amazon RDS - MYSQL database for storing bike data.
c) Flask web server - for hosting the website.
d) Eclipse IDE - for writing all the code.

4. Purpose of the web application:
Provides information on Dublin Bikes bike stations. 

On first opening the application, the user is presented with a google map with icons representing the location of bike stations. On clicking an icon, a table is displayed showing static bike station information for that particular location. 

Below the google map display is another section with three drop-down lists for viewing bike and station availability. When the user selects a bike station, date and time, and clicks the submit button, bike and station availability is displayed in a table below. This table contains all the data gathered for the hour the user selected.

Bike data is available for seven days (9th to 15th April 2017), and the user can select information per hour. All times are in UTC - back end and front end.

5. Technical choices:
a) Amazon EC2 instance - It wasn’t essential to use an EC2 instance for this project, I could have run the API scripts on my laptop. However, I think it is good to know how to set up a remote server and use it - I used this project to practice doing so.

b) Amazon RDS - I could have saved all the json files I retrieved into a folder on my laptop rather than use a remote server and a database, given this is a small project. My choice was again influenced by it being a valuable learning experience and practice.

c) Flask web server - Python Flask is quick to learn, and easy to use. There are better options such as Django. I chose Flask as this was my first project using a web server and I wanted learn the basics before venturing to use a more complex solution such as Django.

d) Eclipse IDE - Eclipse is a robust and versatile IDE. I have been using it for most of my course work.

6. Implementation:
a) Database - I created a BikeData schema with two tables. The first table contains bike station static information (name, address, location, etc) and the second table contains dynamic data (bikes and stations available at a given time). It would have been simpler to create a single table for this small project, but I think it is a good habit to think about how projects scale and provide for it.

b) Getting data from jcdecaux.com API (get_bike_data_from_api.py) - I used python requests to get data from the API. The script contains a timer to retrieve data every fifteen minutes. Had time permitted, I would have learned how to use CRON, the linux scheduler, rather than the timer in the python script. When I ran this script on an EC2 instance, it saved the files it retrieved to a directory on EC2. Each file has a timestamp to its name.

c) Write data to MYSQL database (write_files_to_db_dynamic_data.py and write_files_to_db_static_data.py) - these scripts are also run on EC2. Each connects to the database and writes the contents of the files into the database. To ensure duplicates are not written into the database, the database is queried for the max timestamp and the file written in only if it has a timestamp greater than this max.
 
d) Reading from the database (bikes_data.py) - this script connects to the database and reads from it by passing an SQL query in the form of a string for execution in the database. The result is a tuple which is converted to json. This json object can then be accessed later by Flask.

e) Flask (flask_2.py) - this file first renders the main index.html page at the root url. This script contains three other urls. Function station_show uses bikes_data.py to get data for displaying static bike data on the google map when the user clicks an icon. The function show_station_dynamic uses bikes_data.py to get bike and station availability for the table displayed under the google map when a user makes station and date / time selection. Function show_markers uses  bikes_data.py to get map data.

f) Javascript (main.js) - Initially this script loads the web page with the google map. It uses listeners to listen to user click events. One such click event is when the user clicks an icon on the google map. This script then obtains the relevant json data from flask and uses a string with html in it to display data in index.html. A similar process occurs when the uses makes station, date and time selections and clicks the submit button to display the table.

7. Conclusion:
I enjoyed working on this project as it allowed me to develop a full stack solution in which I learned how all the components I built work together to produce the application. This is the first time I have worked with Flask, or anything like it. The most challenging part for me was displaying the static table of bike information when the user clicks an icon. I solved this problem by creating a div in place as a response to a click event. This div was then passed the html data to display.

