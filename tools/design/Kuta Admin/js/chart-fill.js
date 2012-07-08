$(document).ready(function(){
    var l0 = [6,  11, 10, 13, 11,  7];
    var l1 = [3,   6,  7,  7,  5,  3];
    var l2 = [4,   8,  9, 10, 8,   6];
    var l3 = [9,  13, 14, 16, 17, 19];
    var l4 = [15, 17, 16, 18, 13, 11];
     
    var plot1 = $.jqplot("area-chart-div", [l0, l1, l2, l3, l4], {
        axesDefaults: {
            pad: 1.05
        },
        //////
        // Use the fillBetween option to control fill between two
        // lines on a plot.
        //////
        fillBetween: {
            // series1: Required, if missing won't fill.
            series1: 1,
            // series2: Required, if  missing won't fill.
            series2: 3,
            // color: Optional, defaults to fillColor of series1.
            color: "rgba(227, 167, 111, 0.7)",
            // baseSeries:  Optional.  Put fill on a layer below this series
            // index.  Defaults to 0 (first series).  If an index higher than 0 is
            // used, fill will hide series below it.
            baseSeries: 0,
            // fill:  Optional, defaults to true.  False to turn off fill.  
            fill: true
        },
		grid: {
			borderWidth: 0,
			gridLineColor: '#cdcdcd',    // *Color of the grid lines.
			background: '#f9f9f9',      // CSS color spec for background color of grid.
			shadow: false		
		},
		seriesColors: [ "#a55757", "#9b8250", "#85934b", "#ab552a", "#a87e29", "#5b4347" ],
        seriesDefaults: {
            rendererOptions: {
                //////
                // Turn on line smoothing.  By default, a constrained cubic spline
                // interpolation algorithm is used which will not overshoot or
                // undershoot any data points.
                //////
                smooth: true
            }
        }
    });
});