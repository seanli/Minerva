// Sticky elements
(function($) {
  /**
   * Add our plugin to the jQuery.fn object
   */
  $.fn.sticky = function(options) {
    /**
     * Define some default settings
     */
    var defaults = {
      // #{EDIT-HERE}# Your default options go here ...
    };
    /**
     * Merge the runtime options with the default settings
     */
    var options = $.extend({}, defaults, options);
    /**
     * Iterate through the collection of elements and
     * return the object to preserve method chaining
     */
    return this.each(function(i) {
      /**
       * Wrap the current element in an instance of jQuery
       */
      var $this = $(this);
      $this.waypoint(function(event, direction) {
        if(direction === 'down') {
          elem_width = $this.width();
          $this.addClass('sticky');
          $this.css('width', elem_width);
        } else {
          $this.removeClass('sticky');
          $this.removeAttr('style');
        }
        event.stopPropagation();
      }, {
        onlyOnScroll : true,
      });
    });
  };
})(jQuery);

// Auto-complate elements (extends JQuery UI Autocomplete)
(function($) {
  $.fn.auto_complete = function(options) {
    var defaults = {
      minLength : 1,
      autoFocus : true,
      delay : 200,
      focus : function(event, ui) {
        return false;
      },
      // source : 'url...'
      // select : function(event, ui) { ... }
      // search : function(event, ui) { ... }
      // render : function(ul, item) { ... }
      render : null,
    };
    var options = $.extend({}, defaults, options);
    return this.each(function(i) {
      var $this = $(this);
      if(options.render != null) {
        $this.autocomplete(options).data('autocomplete')._renderItem = options.render;
      } else {
        $this.autocomplete(options);
      }
    });
  };
})(jQuery);

// AJAX forms
(function($) {
  $.fn.ajax_form = function(options) {
    var defaults = {
      preSubmit : function() {},
      trigger : null, // Button element which triggers submit
      appView : '', // The Dajax view called in the format: app.view
      // Callback function is separately declared and called using Dajax mechanism
    };
    var options = $.extend({}, defaults, options);
    return this.each(function(i) {
      var $this = $(this);
      var $trigger = options.trigger;
      $trigger.click(function() {
        var form_id = $this.attr('id');
        // Calls the preSubmit function
        options.preSubmit();
        var form_data = $this.serializeObject(true);
        var appView = options.appView.split('.');
        Dajaxice[appView[0]][appView[1]](Dajax.process, {
          'form_data' : form_data,
          'form_id' : form_id
        });
      });
    });
  };
})(jQuery);
