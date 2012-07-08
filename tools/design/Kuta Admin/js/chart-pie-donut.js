$(document).ready(function(){
  var s1 = [['abcd',16], ['efgh',8], ['ijkl',14], ['mnop',16], ['qrste',8], ['opresf',14]];
   
  var plot3 = $.jqplot('donut-pie-div', [s1], {
	seriesColors: [ "#a55757", "#9b8250", "#85934b", "#ab552a", "#a87e29", "#5b4347" ],  // colors that will
	// be assigned to the series.  If there are more series than colors, colors
	// will wrap around and start at the beginning again.
	seriesDefaults: {
		// make this a donut chart.
		renderer:$.jqplot.DonutRenderer,
		rendererOptions:{
			// Donut's can be cut into slices like pies.
			sliceMargin: 3,
			// Pies and donuts can start at any arbitrary angle.
			startAngle: -90,
			showDataLabels: true,
			shadowOffset: 6,    // offset from the bar edge to stroke the shadow.
			shadowDepth: 1,     // nuber of strokes to make for the shadow.
			shadowAlpha: 0.1,   // transparency of the shadow.
			// By default, data labels show the percentage of the donut/pie.
			// You can show the data 'value' or data 'label' instead.
			dataLabels: 'value'
		}
	},
	grid: {
		borderWidth: 0,
		gridLineColor: '#cdcdcd',    // *Color of the grid lines.
		background: '#f9f9f9',      // CSS color spec for background color of grid.
		shadow: false		
	}
  });
});