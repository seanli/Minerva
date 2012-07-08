//<!-- GOOGLE MAP -->
// We need to bind the map with the "init" event otherwise bounds will be null
$('#visitors-geo').gmap({'zoom': 2, 'disableDefaultUI':true}).bind('init', function(evt, map) { 
	var bounds = map.getBounds();
	var southWest = bounds.getSouthWest();
	var northEast = bounds.getNorthEast();
	var lngSpan = northEast.lng() - southWest.lng();
	var latSpan = northEast.lat() - southWest.lat();
	for ( var i = 0; i < 1000; i++ ) {
		var lat = southWest.lat() + latSpan * Math.random();
		var lng = southWest.lng() + lngSpan * Math.random();
		$('#visitors-geo').gmap('addMarker', { 
			'position': new google.maps.LatLng(lat, lng) 
		}).click(function() {
			$('#visitors-geo').gmap('openInfoWindow', { content : 'Visitors Geolocation' }, this);
		});
	}
	$('#visitors-geo').gmap('set', 'MarkerClusterer', new MarkerClusterer(map, $(this).gmap('get', 'markers')));
	// To call methods in MarkerClusterer simply call 
	// $('#visitors-geo').gmap('get', 'MarkerClusterer').callingSomeMethod();
});