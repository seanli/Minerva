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
