function includeStyle(url){
    var headID = document.getElementsByTagName("head")[0];         
    var cssNode = document.createElement('link');
    cssNode.type = 'text/css';
    cssNode.rel = 'stylesheet';
    cssNode.href = url;
    cssNode.media = 'screen';
    headID.appendChild(cssNode);
}

function includeScript(url){
    var headID = document.getElementsByTagName("head")[0];         
    var newScript = document.createElement('script');
    newScript.type = 'text/javascript';
    newScript.src = url;
    headID.appendChild(newScript);
}


function showOverlay(html) {

   $(document.body).addClass('noscroll');

   var overlay = document.createElement("div");
   overlay.setAttribute("id","overlay");
   overlay.setAttribute("class", "overlay");
   var html_close = "<div class='close' onclick='cleanUp();'><span class='button'>Close</span></div>";
   overlay.innerHTML = html_close + html;
   document.body.appendChild(overlay);

   // hide any flash that may appear over overlay
   $('embed').hide();
    
}

function cleanUp() {
   var overlay = document.getElementById("overlay");
   if (overlay){
       document.body.removeChild(overlay);
   }
   
   // restore body
   $(document.body).removeClass('noscroll');
   $('embed').show();
    
}

var height;
var width;

function showPage(html){
    var html = "<div class='frame'>" + html + "</div>";
    cleanUp();
    showOverlay(html);
}

var MIN_SIZE = 200;

function showPageImages() {
    var html = "";
    var images = document.getElementsByTagName("img");
    if (images.length > 0){
        for (var i = 0; i < images.length; i++){
            var img = images[i];
            if (/* img.clientWidth > MIN_SIZE && */ img.clientHeight > MIN_SIZE){
                var dimensions = img.clientWidth + " x " + img.clientHeight;
                var snippet = "<span class='item_thumb_holder'><span class='item_thumb'><img src='" + img.src + "' onclick='showItem(\""+img.src+"\");'><span class='thumb_dim'>"+dimensions+"</span></span></span>";
                html = html + snippet;
            }
        }
    }
        
    if (!html){
        html = "<span>Sorry, no pictures are big enough to add.</span>";
    }
    
    showPage(html);

}

function showItem(imageUrl){
    var html = "<table class='item_profile'><tr><td class='left'><img src='"+imageUrl+"'></td><td class='right'><fieldset><legend>Style This!</legend><ol><li><label for='name'>Item Name</label><input type='text' name='name' value='"+document.title+"'></li><li><label for='description'>Description</label><textarea name='description' rows='4' cols='50'></textarea><li><label for='price'>Price</label><input type='text' name='price' size='6'><li><label for='url'>Original URL</label><input type='text' name='url' value='"+document.location+"' size='80'><li></ol></fieldset><div class='buttons'><span class='button'>Save</span><span class='button'>Save and Recommend</span></div></td></table>";
    showPage(html);
}

includeStyle('http://127.0.0.1:8000/static/css/tools.css');
includeScript('http://127.0.0.1:8000/static/script/jquery-1.7.1.min.js');
includeScript('http://127.0.0.1:8000/static/script/test.js');
showPageImages();


