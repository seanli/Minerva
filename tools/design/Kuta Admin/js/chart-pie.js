$(document).ready(function(){
  var data = [
    ['Heavy Industry', 12],['Retail', 9], ['Light Industry', 14], 
    ['Out of home', 16],['Commuting', 7], ['Orientation', 9]
  ];
  var plot1 = jQuery.jqplot ('pie-div', [data], 
    {
	seriesColors: [ "#a55757", "#9b8250", "#85934b", "#ab552a", "#a87e29", "#5b4347" ],
	// colors that will
	// be assigned to the series.  If there are more series than colors, colors
	// will wrap around and start at the beginning again.
      seriesDefaults: {
        // Make this a pie chart.
        renderer: jQuery.jqplot.PieRenderer, 
        rendererOptions: {
          // Put data labels on the pie slices.
          // By default, labels show the percentage of the slice.
          showDataLabels: true
        }
      }, 
      legend: { show:true, placement: 'insideGrid', location: 'e' },
		grid: {
			borderWidth: 0,
			gridLineColor: '#cdcdcd',    // *Color of the grid lines.
			background: '#f9f9f9',      // CSS color spec for background color of grid.
			shadow: false		
		}
    }
  );
});