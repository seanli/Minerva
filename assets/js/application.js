// NOTICE!! DO NOT USE ANY OF THIS JAVASCRIPT
// IT'S ALL JUST JUNK FOR OUR DOCS!
// ++++++++++++++++++++++++++++++++++++++++++

! function($) {

	$(function() {
		// tooltip demo
		$('.tooltip-demo.well').tooltip({
			selector : "a[rel=tooltip]"
		})
		// Popover
		$("a[rel=popover]").popover()
	})
	
}(window.jQuery)