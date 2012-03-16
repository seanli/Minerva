// NOTICE!! DO NOT USE ANY OF THIS JAVASCRIPT
// IT'S ALL JUST JUNK FOR OUR DOCS!
// ++++++++++++++++++++++++++++++++++++++++++

! function($) {

	$(window).keypress(function(e) {
	    if (e.which == 13) {
	        var $targ = $(e.target);
	        if (!$targ.is("textarea") && !$targ.is(":button,:submit")) {
	            var focusNext = false;
	            $(this).find(":input:visible:not([disabled],[readonly]), a").each(function(){
	                if (this === e.target) {
	                    focusNext = true;
	                }
	                else if (focusNext){
	                    $(this).focus();
	                    return false;
	                }
	            });
	            return false;
	        }
	    }
	});
	
	$(function() {
		// tooltip demo
		$('.tooltip-demo.well').tooltip({
			selector : "a[rel=tooltip]"
		})
		// Popover
		$("a[rel=popover]").popover()
	})
	
	/* Update datepicker plugin so that MM-DD-YYYY format is used. */
	$.extend($.fn.datepicker.defaults, {
		parse : function(string) {
			var matches;
			if(( matches = string.match(/^(\d{2,2})\/(\d{2,2})\/(\d{4,4})$/))) {
				return new Date(matches[3], matches[1] - 1, matches[2]);
			} else {
				return null;
			}
		},
		format : function(date) {
			var month = (date.getMonth() + 1).toString(), dom = date.getDate().toString();
			if(month.length === 1) {
				month = "0" + month;
			}
			if(dom.length === 1) {
				dom = "0" + dom;
			}
			return month + "/" + dom + "/" + date.getFullYear();
		}
	});

}(window.jQuery)