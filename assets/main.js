$(document).ready(function () { 
	$('form#create').on('change', 'input[type="file"]', function (){
		$('form#create').append('<input name="file[]" type="file" multiple>');
	})	
})