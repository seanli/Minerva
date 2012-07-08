$(document).ready(function() {
	$('.datepicker').datepicker();
	$('.dropdown-timepicker').timepicker({
		defaultTime: 'current',
		minuteStep: 15,
		disableFocus: true,
		template: 'dropdown'
	});
	$(".chzn-select").chosen();
	$(".chzn-select-deselect").chosen({allow_single_deselect:true});
	$('.alert-message a.close').live('click', function(){
		$(this).parent().parent('.c-alert').slideUp('slow');
	});
	$('.bottom_tooltip').tooltip({
		placement: 'bottom'
	});
	$('.left_tooltip').tooltip({
		placement: 'left'
	});
	$('.right_tooltip').tooltip({
		placement: 'right'
	});
	$('.top_tooltip').tooltip();
	$('.dropdown-menu.dropdown-user-account').click(function(event){
		event.stopPropagation();
	});
	$('#myEditor').wysihtml5();
	$('.accordion-body.collapse.in').prev('.accordion-heading').addClass('acc-active');
	$('.accordion-heading').live('click', function(){
		$('.accordion-heading').removeClass('acc-active');
		$(this).addClass('acc-active');
	});
	$('#example').dataTable({
		"sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span4'i><'span8'p>>",
		"sPaginationType": "bootstrap",
		"oLanguage": {
			"sLengthMenu": "_MENU_ records per page"
		}
	});
});