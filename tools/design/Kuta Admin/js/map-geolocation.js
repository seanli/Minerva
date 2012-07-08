$('#map-geolocation-div').gmap().bind('init', function(evt, map) {
	$('#map-geolocation-div').gmap('getCurrentPosition', function(position, status) {
		if ( status === 'OK' ) {
			var clientPosition = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
			$('#map-geolocation-div').gmap('addMarker', {'position': clientPosition, 'bounds': true});
			$('#map-geolocation-div').gmap('option', 'zoom', 15);
		}
	});   
});