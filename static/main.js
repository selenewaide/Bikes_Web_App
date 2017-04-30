var bikeContainer = document.getElementById("bike_info")

var btn = document.getElementById("station_30");
btn.addEventListener("click", get_station);

btn = document.getElementById("station_102");
btn.addEventListener("click", get_station);

function get_station_by_event(e) {
	console.log(e);
	station_id = e.target.id;

	var station_num = station_id.substring(8);
	get_station(station_num);
}

function get_station(station_num) {
	var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET', '/station/' + station_num);

	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		renderHTML(ourData, station_num);
	};

	ourRequest.send();
}

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


function initMap() {

	var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET', '/markers');

	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);

		var uluru = {lat: 53.340962, lng: -6.265305};
		var map = new google.maps.Map(document.getElementById('map'), {
			zoom: 13,
			center: uluru
		});

		for (var i = 0; i < ourData.lat.length; i++) {
			
			var contentString = "This is my test";
			var infowindow = new google.maps.InfoWindow({
		          content: contentString,
		          maxWidth: 200
		        });
			
			//var uluru = {lat: ourData.lat[i], lng: ourData.lng[i]}
			console.log(ourData.lat[i], ourData.lng[i]);
			var marker = new google.maps.Marker({
				position: {lat: ourData.lat[i], lng: ourData.lng[i]},
				map: map,
				station_id: i
			});
			
			addInfoWindow(map, marker, infowindow);
		};
	};

	ourRequest.send();
}

function addInfoWindow(map, marker, infowindow) {
	marker.addListener('click', function() {
		infowindow.setContent('<div id="stationinfo_' + marker.get('station_id') + '">Loading station info for station ' + marker.get('station_id') + '...</div>');
		infowindow.open(map, marker);
		get_station(marker.get('station_id'));
	});
}

