function confirmModal(options) {
  var defaults = {
      heading: 'Please Confirm Action',
      message: 'The action requested may be irreversible.<br />Do you wish to continue?',
      yes: 'Yes',
      no: 'No',
      callback : null
  };
  var options = $.extend(defaults, options);
  
  var html = '<div class="modal fade" id="confirmModal"><div class="modal-header"><a class="close" data-dismiss="modal">×</a>' +
            '<h3>#Heading#</h3></div><div class="modal-body">' +
            '#Message#</div><div class="modal-footer">' +
            '<a href="#" class="btn btn-primary" id="confirmYesBtn">#Yes#</a>' +
            '<a href="#" class="btn" data-dismiss="modal">#No#</a></div></div>';
  html = html.replace('#Heading#', options.heading).replace('#Message#', options.message).replace('#Yes#', options.yes).replace('#No#', options.no);
  $('body').append(html);
  $('#confirmModal').modal('show');
  $('#confirmYesBtn').click(function() {
      if(options.callback != null)
          options.callback();
      $('#confirmModal').modal('hide');
  });
};

! function($) {

  $(window).keypress(function(e) {
    if(e.which == 13) {
      var $targ = $(e.target);
      if(!$targ.is("textarea") && !$targ.is(":button,:submit")) {
        var focusNext = false;
        $(this).find(":input:visible:not([disabled],[readonly]), a").each(function() {
          if(this === e.target) {
            focusNext = true;
          } else if(focusNext) {
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