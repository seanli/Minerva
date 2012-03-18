// Raise a confirmation modal dialog
function confirmModal(options) {
  var defaults = {
      heading: 'Please Confirm Action',
      message: 'The action requested may be irreversible.<br />Do you wish to continue?',
      yes: 'Yes',
      no: 'No',
      callback: null
  };
  var options = $.extend(defaults, options);
  
  var html = '<div class="modal fade" id="confirmModal"><div class="modal-header"><a class="close" data-dismiss="modal">&times;</a>' +
            '<h3>#Heading#</h3></div><div class="modal-body">' +
            '#Message#</div><div class="modal-footer">' +
            '<a href="#" class="btn btn-danger" id="confirmYesBtn">#Yes#</a>' +
            '<a href="#" class="btn" data-dismiss="modal">#No#</a></div></div>';
  html = html.replace('#Heading#', options.heading).replace('#Message#', options.message).replace('#Yes#', options.yes).replace('#No#', options.no);
  $('body').append(html);
  $('#confirmModal').modal('show');
  $('#confirmYesBtn').click(function() {
      if (options.callback != null)
          options.callback();
      $('#confirmModal').modal('hide');
  });
  $('#confirmModal').on('hidden', function() {
    $(this).remove();
  });
};

// Prevent form submission from pressing Enter key
$(document).ready(function() {
  $(window).keypress(function(e) {
    if (e.which == 13) {
      var $targ = $(e.target);
      if (!$targ.is("textarea") && !$targ.is(":button,:submit")) {
        var focusNext = false;
        $(this).find(":input:visible:not([disabled],[readonly]), a").each(function() {
          if (this === e.target) {
            focusNext = true;
          } else if (focusNext) {
            $(this).focus();
            return false;
          }
        });
        return false;
      }
    }
  });
});
