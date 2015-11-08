//
// handler functions for button click events
//

function onDoorClicked(obj, id) {
  var xhttp;
  
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  if (xhttp.readyState == 4 && xhttp.status == 200) {
    document.getElementById('response_text').innerHTML = xhttp.responseText;
    }
  }
  xhttp.open('GET', '/door?id='+id, true);
  xhttp.send();
}

function onCameraClicked(obj, id) {
  var xhttp;
  var cam_pos = { 'l-cam': 'left', 'm-cam': 'middle', 'r-cam': 'right'};
  
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  if (xhttp.readyState == 4 && xhttp.status == 200) {
    document.getElementById('cam_response_text').innerHTML = xhttp.responseText;
    // add time to request to act as cachebreaker
    // i.e. photo will be loaded again instead of being cached
    document.getElementById(cam_pos[id]).src='my_image.png?' + new Date().getTime();
    }
  }
  xhttp.open('GET', '/cam?id='+id, true);
  xhttp.send();
}
