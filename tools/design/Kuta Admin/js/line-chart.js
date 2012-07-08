$(document).ready(function(){
  // Some simple loops to build up data arrays.
  var cosPoints = [];
  for (var i=0; i<2*Math.PI; i+=0.4){ 
    cosPoints.push([i, Math.cos(i)]); 
  }
    
  var sinPoints = []; 
  for (var i=0; i<2*Math.PI; i+=0.4){ 
     sinPoints.push([i, 2*Math.sin(i-.8)]); 
  }
    
  var powPoints1 = []; 
  for (var i=0; i<2*Math.PI; i+=0.4) { 
      powPoints1.push([i, 2.5 + Math.pow(i/4, 2)]); 
  }
    
  var powPoints2 = []; 
  for (var i=0; i<2*Math.PI; i+=0.4) { 
      powPoints2.push([i, -2.5 - Math.pow(i/4, 2)]); 
  } 
 
  var plot3 = $.jqplot('line-chart-div', [cosPoints, sinPoints, powPoints1, powPoints2], 
    { 
      title:'Line Style Options',
		grid: {
			borderWidth: 0,
			gridLineColor: '#cdcdcd',    // *Color of the grid lines.
			background: '#f9f9f9',      // CSS color spec for background color of grid.
			shadow: false		
		},
		seriesColors: [ "#a55757", "#9b8250", "#85934b", "#ab552a", "#a87e29", "#5b4347" ],
      // Series options are specified as an array of objects, one object
      // for each series.
      series:[ 
          {
            // Change our line width and use a diamond shaped marker.
            lineWidth:2, 
            markerOptions: { style:'dimaond' }
          }, 
          {
            // Don't show a line, just show markers.
            // Make the markers 7 pixels with an 'x' style
            showLine:false, 
            markerOptions: { size: 7, style:"x" }
          },
          { 
            // Use (open) circlular markers.
            markerOptions: { style:"circle" }
          }, 
          {
            // Use a thicker, 5 pixel line and 10 pixel
            // filled square markers.
            lineWidth:5, 
            markerOptions: { style:"filledSquare", size:10 }
          }
      ]
    }
  );
    
});