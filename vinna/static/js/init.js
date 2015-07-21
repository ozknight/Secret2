(function($){
  $(function(){
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

  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function(){
//$('.materialboxed').materialbox();
//$('.parallax').parallax();
$('.materialboxed').materialbox();
$('.collapsible').collapsible();
});