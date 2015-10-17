//hw: save, make the canvas mirror the image then save the canvas to a file
//HW: ZOOM in/out(touchpad or button) and navigate(see issues on github) track the scale in a float variable
//hw: MAKE Amazon AWS account and look into amazon s3
//hw: download SqlPro (freeware)

$(document).ready(function(){
	var canvas      = document.createElement('canvas'),
		context     = canvas.getContext('2d'),
		img         = $('img#image')[0],
		$imgWrapper = $('div#image-workspace');

	//input, draw to canvas
	$('input#image-upload').on('change', function (event) {
    	
    	img.src = URL.createObjectURL(event.target.files[0]);

    	img.onload = function() {
    		canvas.height = this.height;
    		canvas.width = this.width;
    		context.drawImage(img, 0, 0, img.width, img.height);	
    	}
	});
	//rectangular selector
    $('div#image-workspace').on('mousedown', function (event) {
        var startTop = event.pageY,
            startLeft = event.pageX,
            $box = $('<div id="selection"></div>');

        $('#selection').remove();
        $('body').append($box);

        $(window).on('mousemove', function (event) {
            var top = startTop,
                left = startLeft,
                bottom = event.pageY,
                right = event.pageX,
                height = Math.abs(bottom - top),
                width = Math.abs(right - left);

            event.preventDefault();

            if (bottom < top) top = bottom;
            if (right < left) left = right;

            $box.css({
                top: top + 'px',
                left: left + 'px',
                height: height + 'px',
                width: width + 'px'
            })

            console.log(top, left, height, width);
        });

        $(window).one('mouseup', function (event){ //one instead of on to stop the possibility of MANY mouseup listeners
            $(window).off('mousemove');
        });
    });
 
	$('button#save').on('click', function () {
		document.location.href = canvas.toDataURL('image/png').replace('image/png', 'image/octet-stream');
	});

	$('button#zoom-in').on('click', function () {
		var value = $(this).val();
		
		if(value ==='OFF') {
			value = 'ON';
		}
		else {
			value = 'OFF'
		};

		if (value === 'ON') {
			$('img#image').on('click', function () {	
				var ratio  = img.height/img.width,
					resize = 1.1,
					mouseX = event.pageX,
					mouseY = event.pageY,
					newH   = img.height * resize,
					newW   = img.width * resize,
					imgDiv = img.parentNode;

				img.style.height = newH + 'px';
				img.style.width = newW + 'px';
				
				console.log(mouseX, mouseY);

				imgDiv.scrollLeft = (mouseX * resize) - (newW/2)/2;
				imgDiv.scrollTop  = (mouseY * resize) - (newH/2)/2;
			});
		}

		else {
			$('img#image').off('click');
		};
	});

	$('button#zoom-out').on('click', function () {
		var value = $(this).val();
		
		if(value ==='OFF') {
			value = 'ON';
		}
		else {
			value = 'OFF'
		};

		if (value === 'ON') {
			$('img#image').on('click', function () {	
				var ratio  = img.height/img.width,
					resize = 0.9,
					mouseX = event.pageX,
					mouseY = event.pageY,
					newH   = img.height * resize,
					newW   = img.width * resize,
					imgDiv = img.parentNode;

				img.style.height = newH + 'px';
				img.style.width = newW + 'px';
				
				console.log(mouseX, mouseY);

				imgDiv.scrollLeft = (mouseX * resize) - (newW/2)/2;
				imgDiv.scrollTop  = (mouseY * resize) - (newH/2)/2;
			});
		}

		else {
			$('img#image').off('click');
		};
	});


});



