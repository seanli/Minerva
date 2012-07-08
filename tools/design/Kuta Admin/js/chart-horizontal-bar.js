$(document).ready(function(){
	// For horizontal bar charts, x an y values must will be "flipped"
	// from their vertical bar counterpart.
	var plot2 = $.jqplot('horizontal-bar-div', [
		[[2,1], [4,2], [6,3], [3,4]], 
		[[5,1], [1,2], [3,3], [4,4]], 
		[[4,1], [7,2], [1,3], [2,4]]], {
		
		seriesColors: [ "#a55757", "#9b8250", "#85934b" ],  // colors that will
		// be assigned to the series.  If there are more series than colors, colors
		// will wrap around and start at the beginning again.
		
		seriesDefaults: {
			renderer:$.jqplot.BarRenderer,
			// Show point labels to the right ('e'ast) of each bar.
			// edgeTolerance of -15 allows labels flow outside the grid
			// up to 15 pixels.  If they flow out more than that, they 
			// will be hidden.
			pointLabels: { show: true, location: 'e', edgeTolerance: -15 },
			// Rotate the bar shadow as if bar is lit from top right.
			// shadow: false,   // show shadow or not.
			// Here's where we tell the chart it is oriented horizontally.			
			rendererOptions: {						
				barPadding: 0,      // number of pixels between adjacent bars in the same
									// group (same category or bin).
				barMargin: 10,      // number of pixels between adjacent groups of bars.
				barDirection: 'horizontal', // vertical or horizontal.
				barWidth: null,     // width of the bars.  null to calculate automatically.
				shadowOffset: 0,    // offset from the bar edge to stroke the shadow.
				shadowDepth: 3,     // nuber of strokes to make for the shadow.
				shadowAlpha: 0.6,   // transparency of the shadow.
			}
		},
		// Custom labels for the series are specified with the "label"
		// option on the series option.  Here a series option object
		// is specified for each series.
		series:[
			{label:'Label 1'},
			{label:'Label 2'},
			{label:'Label 3'}
		],
		grid: {
			borderWidth: 0,
			gridLineColor: '#cdcdcd',    // *Color of the grid lines.
			background: '#f0f0f0',      // CSS color spec for background color of grid.
			shadow: false
		},
		// Show the legend and put it inside the grid.
		legend: {
			show: true,
			placement: 'insideGrid',
			location: 'ne'
		},
		axes: {
			yaxis: {
				renderer: $.jqplot.CategoryAxisRenderer
			}
		}
	});
});