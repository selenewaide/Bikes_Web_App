var bikeContainer = document.getElementById("bike_info")

// button to submit drop down selection
var btn = document.getElementById("submit_btn");
btn.addEventListener("click", show_bike_table);

// display table below google map - per drop down selection
function show_bike_table() {
	
	// station selected
	var station_selected = document.getElementById("station_id_dd");
	var strUser1 = station_selected.options[station_selected.selectedIndex].value;
	strUser1 = parseInt(strUser1)
	
	// date selected
	var date_selected = document.getElementById("date_dd");
	var strUser2 = date_selected.options[date_selected.selectedIndex].value;
	strUser2 = parseInt(strUser2)
	
	// time selected
	var time_selected = document.getElementById("time_id_dd");
	var strUser3 = time_selected.options[time_selected.selectedIndex].value;
	strUser3 = parseInt(strUser3)
	
	// get data from DB with arguments: station and timestamps (composed from selections above)
	get_station_dynamic(strUser1, (strUser2+strUser3), (strUser2+strUser3+3599));
	
}

// obtaining station id from google map icon click
// calling get_station with the station id as argument
function get_station_by_event(e) {
	station_id = e.target.id;

	var station_num = station_id.substring(8);
	get_station(station_num);
}

// gets json data using request
// calls function with html string and passes in this data
// for display of station station data at google map icon on click
function get_station(station_num) {
	var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET', '/station/' + station_num);

	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		renderHTML(ourData, station_num);
	};

	ourRequest.send();
}

//html string using data from request
//for display of station station data at google map icon on click
function renderHTML(data, station_num) {
	var htmlString = "";

	htmlString += "<table><tr><th>Station</th><td>" 
		+ data.station + "</td></tr>";
	htmlString += "<table><tr><th>Address</th><td>" 
		+ data.address + "</td></tr>";
	htmlString += "<table><tr><th>Lat</th><td>" 
		+ data.lat + "</td></tr>";
	htmlString += "<table><tr><th>Lng</th><td>" 
		+ data.lng + "</td></tr>";
	htmlString += "<table><tr><th>Bike Stands</th><td>" 
		+ data.bike_stands + "</td></tr>";
	htmlString += "</table>";

	var infocontainer = document.getElementById('stationinfo_' + station_num);
	infocontainer.innerHTML = htmlString;
}

//gets json data using request
//calls function with html string and passes in this data
//for display of dynamic station station below the google map
function get_station_dynamic(station_num, timestamp_from, timestamp_to) {
	var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET', '/station/' + station_num + '/' +  timestamp_from + '/' + timestamp_to);

	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		renderHTML_Dynamic(ourData, station_num);
	};

	ourRequest.send();
}

//html string using data from request
//for display of dynamic station station below the google map
function renderHTML_Dynamic(data, station_num) {
	console.log(data);
	var htmlString = "";
    htmlString += "<table>";
    
    htmlString += "<tr>" + "<th>Station</th>" + 
        "<th>Name</th>" + 
        "<th>Number of Stands</th>" + 
        "<th>Available Stands</th>" + 
        "<th>Available Bikes</th>" + 
        "<th>Latitude</th>" + 
        "<th>Longitude</th>" + 
        "<th>Date & Time</th>" +
        "</tr>";
    
    
    for (i = 0; i < data.station.length; i++) {
    	
    	var date_time = (new Date(data.last_update[i]*1000)).toUTCString() 
    	
    	
        htmlString += "<tr>" + "<td>" + data.station[i] + "</td>" + 
            "<td>" + data.address[i] + "</td>" +
            "<td>" + data.bike_stands[i] + "</td>" +
            "<td>" + data.available_bike_stands[i] + "</td>" +
            "<td>" + data.available_bikes[i] + "</td>" +
            "<td>" + data.lat[i] + "</td>" +
            "<td>" + data.lng[i] + "</td>" +
            "<td>" + date_time + "</td>" +
            "</tr>";
    }
    
    htmlString += "</table>";

	var infocontainer = document.getElementById('dynamic_table');
	infocontainer.innerHTML = htmlString;
}


// displays google map and icons
function initMap() {

	var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET', '/markers');

	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		
		var map_position = {lat: 53.340962, lng: -6.265305}; // default lat and lng
		var map = new google.maps.Map(document.getElementById('map'), {
			zoom: 13,
			center: map_position
		});
		
		var htmlString1 = "";
		
		// adding icons to map using lat and lng from bike data
		for (var i = 0; i < ourData.lat.length; i++) {
			
			var contentString = "";
			var infowindow = new google.maps.InfoWindow({
		          content: contentString,
		          maxWidth: 200
		        });
			
			var marker = new google.maps.Marker({
				position: {lat: ourData.lat[i], lng: ourData.lng[i]},
				map: map,
				station_id: ourData.station[i]
			});
			
			addInfoWindow(map, marker, infowindow);
			
			// populating the drop-down list for station names
		    htmlString1 += "<option value='" + ourData.station[i] + "'>" + ourData.address[i] + "</option>";
			
		}
		
		// populating the drop-down list for time
		var htmlString2 = "";
		for (var i = 0; i <= 23; i++) {
			htmlString2 += "<option value='" + (i*3600) + "'>" + i + "</option>";
		}
		
		var infocontainer2 = document.getElementById('time_id_dd');
		infocontainer2.innerHTML = htmlString2;
		
		var infocontainer = document.getElementById('station_id_dd');
		infocontainer.innerHTML = htmlString1;
		
	};
	
	ourRequest.send();
}

// google map event listener to display bike info on click of icon
// creates a div in place when the icon is clicked
// this is to display the static bike data per icon
function addInfoWindow(map, marker, infowindow) {
	marker.addListener('click', function() {
		infowindow.setContent('<div id="stationinfo_' + marker.get('station_id') + '">Loading station info for station ' + marker.get('station_id') + '...</div>');
		infowindow.open(map, marker);
		get_station(marker.get('station_id'));
	});
}

