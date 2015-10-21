$(document).ready(function () { 
	$('form#create').on('change', 'input[type="file"]', function (){
		$('div#photo-upload').append('<p><input name="file[]" type="file" multiple></p>');
	})	
})