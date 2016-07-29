$(document).ready(function () { 
	var upload = $('#upload-photos');
	upload.click(function() {
		upload.off()
		var area = $('#upload-photos');

		area.append('<div id="upload-area"><label for="files">Select multiple files: <br> Click here!</label><input id="files" name="file[]" type="file" multiple/> <output id="result" /></div>');
	    //Check File API support
	    var div = document.createElement("div");
	    div.classList.add('row');
	    if(window.File && window.FileList && window.FileReader)
	    {
	        var filesInput = document.getElementById("files");
	        
	        filesInput.addEventListener("change", function(event){
	            
	            var files = event.target.files; //FileList object
	            var output = document.getElementById("result");
	            
	            $('.upload-thumbnail').remove();

	            for(var i = 0; i< files.length; i++) {
	                var file = files[i];
	                
	                //Only pics
	                if(!file.type.match('image'))
	                  continue;
	                
	                var picReader = new FileReader();
	                
	                picReader.addEventListener("load",function(event){
	                    
	                    var picFile = event.target;
	                    
	                    

	                    
	                    
	                    div.innerHTML += "<div class='col-xs-12 col-sm-6 col-md-4 col-lg-3'><img class='upload-thumbnail' src='" + picFile.result + "'" +
	                            "title='" + picFile.name + "'/>";
	                    
	                    output.insertBefore(div,null);            
	                
	                });
	                
	                 //Read the image
	                picReader.readAsDataURL(file);
	            }                               
	           
	        });
	    }
	    else
	    {
	        console.log("Your browser does not support File API");
	    }
	})


})