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
