(function ($) {

	"use strict";

	// Preload
	$(window).on('load', function () { // makes sure the whole site is loaded
		$('[data-loader="circle-side"]').fadeOut(); // will first fade out the loading animation
		$('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
		$('body').delay(350).css({
			'overflow': 'visible'
		});
	})
    window.form = {};
   	// Wizard
	$("#wizard_container").wizard({
	    stepsWrapper: "#wrapped",
	    submit: ".submit",
	    beforeSelect: function(event, state) {
	        if ($('input#website').val().length != 0) {
	            return false;
	        }
	        if (!state.isMovingForward)
	            return true;
	        var inputs = $(this).wizard('state').step.find(':input');
	        if(!inputs.length || !!inputs.valid()){
	           // validated, we can move, we collect form
	           for(var i=0;i<inputs.length;i++){
	               console.log(inputs[i].value,inputs[i].value);
	               //window.form[''+inputs[i].name] = inputs[i].value;
	           }
	        }
	        return !inputs.length || !!inputs.valid();
	    }
	}).validate({
	    errorPlacement: function(error, element) {
	        if (element.is(':radio') || element.is(':checkbox')) {
	            error.insertBefore(element.next());
	        } else {
	            error.insertAfter(element);
	        }
	    }
	});

	//  progress bar
	$("#progressbar").progressbar();
	$("#wizard_container").wizard({
	    afterSelect: function(event, state) {
	        $("#progressbar").progressbar("value", state.percentComplete);
	        $("#location").text("(" + state.stepsComplete + "/" + state.stepsPossible + ")");
	    }
	});

	// Validate select
	$('#wrapped').validate({
	    ignore: [],
	    rules: {
	        select: {
	            required: true
	        }
	    },
	    errorPlacement: function(error, element) {
	        if (element.is('select:hidden')) {
	            error.insertAfter(element.next('.nice-select'));
	        } else {
	            error.insertAfter(element);
	        }
	    }
	});



	// Modal Help
	$('#modal_h').magnificPopup({
		type: 'inline',
		fixedContentPos: true,
		fixedBgPos: true,
		overflowY: 'auto',
		closeBtnInside: true,
		preloader: false,
		midClick: true,
		removalDelay: 300,
		closeMarkup: '<button title="%title%" type="button" class="mfp-close"></button>',
		mainClass: 'my-mfp-zoom-in'
	});

})(window.jQuery);