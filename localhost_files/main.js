//hw: save, make the canvas mirror the image then save the canvas to a file
//HW: ZOOM in/out(touchpad or button) and navigate(see issues on github) track the scale in a float variable


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
			changeCanvasCallback(canvas, context);
    	};
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

        });

        $(window).one('mouseup', function (event){ //one instead of on to stop the possibility of MANY mouseup listeners
            $(window).off('mousemove');
        });
    });
 
	$('button#zoom-in').on('click', function () {
		var $this = $(this);
		
		if($this.val() === 'OFF') {
			$this.val('ON');
			document.getElementById('zoom-in').className = 'btn btn-success';
		}
		else {
			$this.val('OFF');
			document.getElementById('zoom-in').className = 'btn btn-danger';
		}

		if ($this.val() === 'ON') {
			$('img#image').on('click', function () {	
				var ratio  = img.height/img.width,
					resize = 1.1,
					mouseX = event.pageX,
					mouseY = event.pageY,
					newH   = img.height * resize,
					newW   = img.width * resize,
					imgDiv = img.parentNode;

				event.preventDefault();

				img.style.height = newH + 'px';
				img.style.width = newW + 'px';
				
				console.log(mouseX, mouseY);

				imgDiv.scrollLeft = (mouseX * resize) - (newW/2)/2;
				imgDiv.scrollTop  = (mouseY * resize) - (newH/2)/2;
			});
		}

		else {
			$('img#image').off('click');
		}
	});

	$('button#zoom-out').on('click', function () {
		var $this = $(this);
		
		if($this.val() === 'OFF') {
			$this.val('ON');
			document.getElementById('zoom-out').className = 'btn btn-success';
		}
		else {
			$this.val('OFF');
			document.getElementById('zoom-out').className = 'btn btn-danger';
		};

		if ($this.val() === 'ON') {
			$('img#image').on('click', function () {	
				var ratio  = img.height/img.width,
					resize = 0.9,
					mouseX = event.pageX,
					mouseY = event.pageY,
					newH   = img.height * resize,
					newW   = img.width * resize,
					imgDiv = img.parentNode;

				event.preventDefault();

				img.style.height = newH + 'px';
				img.style.width = newW + 'px';
				
				console.log(mouseX, mouseY);
				//use jquery to get the workspace, use offset to get top and left and get height and width then depending on where you
				//click to zoom in or out use that info to recenter the image.
				imgDiv.scrollLeft = (mouseX * resize) - (newW/2)/2;
				imgDiv.scrollTop  = (mouseY * resize) - (newH/2)/2;
			});
		}

		else {
			$('img#image').off('click');
		};
	});

	//nav around image 
	$('button#nav').on('click', function () {
		var $this = $(this);
		
		if ($this.val() === 'OFF'){
			$this.val('ON');
			document.getElementById('nav').className = 'btn btn-success';
		}

		else {
			$this.val('OFF');
			document.getElementById('nav').className = 'btn btn-danger';
		}

		$('img#image').on('mousedown', function () {
			var startX  = event.pageX,
				startY  = event.pageY;
				imgLeft = img.offsetLeft,
				imgTop  = img.offsetTop;

			$(window).on('mousemove', function() {
				var	clickX   = event.pageX,
					clickY   = event.pageY,
					offsetX  = clickX - startX,
					offsetY  = clickY - startY;

				img.style.position = 'fixed';
				img.style.top = imgTop + offsetY + 'px';
				img.style.left = imgLeft + offsetX + 'px';

			});

			$(window).one('mouseup', function () {
				$(window).off('mousemove');
			});
		});

	});

	function changeCanvasCallback (canvas, context) {
		var href = canvas.toDataURL('image/png');
		$('a#save').prop('href', href);
		// set listener on filename for change and set download property on a tag to change filename
	}

});



