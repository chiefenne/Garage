//
// handler functions for button click events
//

function onDoorClicked(obj, id) {
  var request;
  var textid;
  request = new XMLHttpRequest();
  textid = 'response_text'

  // disable clicking until relay action finished
  document.getElementById('pedestrian').style.pointerEvents = 'none';
  document.getElementById('gate').style.pointerEvents = 'none';
  
  if (id == 'pedestrian') {
      message = 'Side gate operating'
  } else { 
      message = 'Car gate operating'
  }

  document.getElementById(textid).innerHTML = message;
  setTimeout(function() {
      clearResponseText(textid);
  }, 2000);
 
  request.onreadystatechange = function() {

    // enable clicking after relay action finished
    document.getElementById('pedestrian').style.pointerEvents = 'auto';
    document.getElementById('gate').style.pointerEvents = 'auto';
  }
  }
 
  request.open('GET', '/door?id='+id, true);
  request.send();

}

function onCameraClicked(obj, id) {
  var image;
  var request;
  var textid;
  request = new XMLHttpRequest();
  textid = 'cam_response_text'
  var cam_pos = { 'l-cam': 'left', 'm-cam': 'middle', 'r-cam': 'right'};

  if (id == 'l-cam') {
    message = 'Photo has been taken'
  } else { 
    message = 'Photo has been taken'
  }

  document.getElementById(textid).innerHTML = message;
  setTimeout(function() {
      clearResponseText(textid);
  }, 2000);
 
  request.onreadystatechange = function() {
  if (request.readyState == 4 && request.status == 200) {

    if (request.responseText == 'Default image') {
      image = 'placeholder.png'
    } else { 
      image = 'camera.png'
    }
    // add current time to request to act as cachebreaker
    // i.e. photo will be loaded again instead of being cached
    document.getElementById(cam_pos[id]).src=image + '?' + new Date().getTime();
    }
  }

  request.open('GET', '/cam?id='+id, true);
  request.send();
}

function clearResponseText(id) {
  document.getElementById(id).innerHTML = ' '
}
