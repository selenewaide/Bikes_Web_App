
from flask import Flask, render_template
import lib.bikes_data as bikes_data

app = Flask(__name__)

# @ signifies a decorator -
# a way to wrap a function and modify its behaviour
# mapping a url ('/') to a return value in the function
# this is the route url


@app.route("/")
def main():
    return render_template("index.html")

# url for station id


@app.route('/station/<int:station_id>')
def show_station(station_id):

    # get static station data for display on the google map
    station_data = bikes_data.get_static_station_data(station_id)

    # to ensure the browser recognises the json data as json type
    response = app.response_class(
        response=station_data,
        status=200,
        mimetype='application/json'
    )
    return response


# url for station, date and time
@app.route('/station/<int:station_id>/<int:timestamp_from>/<int:timestamp_to>')
def show_station_dynamic(station_id, timestamp_from, timestamp_to):

    # get dynamic data for diplay in a table below the google map
    dynamic_data = bikes_data.get_dynamic_station_data(
        station_id, timestamp_from, timestamp_to)

    # to ensure the browser recognises the json data as json type
    response = app.response_class(
        response=dynamic_data,
        status=200,
        mimetype='application/json'
    )
    return response


# icons on the google map
@app.route('/markers')
def show_markers():

    # get map
    markers_data = bikes_data.get_map_data()

    # to ensure the browser recognises the data as json type
    marker_response = app.response_class(
        response=markers_data,
        status=200,
        mimetype='application/json'
    )
    return marker_response


if __name__ == "__main__":
    app.run(debug=True)
