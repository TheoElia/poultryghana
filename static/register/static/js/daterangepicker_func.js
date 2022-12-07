	/*  Wizard */
	jQuery(function ($) {
		"use strict";
		$('#dates').daterangepicker({
            locale: {
                format: 'DD-MM-YYYY'
            },
            parentEl: "#inline-calendar",
            minDate:new Date(),
            autoUpdateInput: false,
            linkedCalendars:true,
            alwaysShowCalendars: true,
            singleDatePicker: false,
            autoApply :true,
            inline: true
        });
		 	$('#dates').on('apply.daterangepicker', function(ev, picker) {
		  	$(this).val(picker.startDate.format('MM-DD-YY') + ' > ' + picker.endDate.format('MM-DD-YY'));
	  	});
	  		$('#dates').on('cancel.daterangepicker', function(ev, picker) {
		  	$(this).val('');
	  	});
	});
