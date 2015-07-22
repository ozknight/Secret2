(function($){
  $(function(){
    'use strict';
  	function is_touch_device() {
      try {
        document.createEvent("TouchEvent");
        return true;
      } catch (e) {
        return false;
      }
    }
    if (is_touch_device()) {
      $('#nav-mobile').css({ overflow: 'auto'});
    }

    $('.button-collapse').sideNav();
    $('.modal-trigger').leanModal();
    $(".dropdown-button").dropdown({
    	constrain_width: false,
     	hover: false,
    });
    $('.materialboxed').materialbox();
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.datepicker').pickadate({
      selectMonths: true,
      selectYears: 90,
      format: 'mm/dd/yyyy'
    });
    $('.tooltipped').tooltip({
      delay: 50
    });
    $('.scrollspy').scrollSpy();
  });
})(jQuery);