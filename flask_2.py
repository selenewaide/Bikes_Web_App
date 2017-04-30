
from flask import Flask, render_template
import lib.bikes_data as bikes_data

app = Flask(__name__)

# @ signifies a decorator - 
# a way to wrap a function and modify its behaviour
# mapping a url ('/') to a return value in the function
@app.route("/main")
def main():
    return render_template("index.html")

@app.route('/station/<int:station_id>')
def show_station(station_id):
    
    # run bikes_data.get_static_station_data with station number
    station_data = bikes_data.get_static_station_data(station_id)
    
    # to ensure the browser recognises the json data as json type
    response = app.response_class(
        response=station_data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/markers')
def show_markers():
    
    # run bikes_data.get_static_station_data 
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
