//
// handler functions for button click events
//

function onDoorClicked(obj, id) {

  // disable further clicking until relay action finished
  deActivateClick();

  var request;
  var textid;
  request = new XMLHttpRequest();
  textid = 'response_text'
  
  if (id == 'pedestrian') {
      message = 'Side gate operating'
  } else { 
      message = 'Car gate operating'
  }

  document.getElementById(textid).innerHTML = message;
  // clear message after 2 seconds
  clearResponseText(textid, 2000);

  setTimeout(function() {
      document.getElementById(textid).innerHTML = ' '
  }, 2000);
 
  request.onreadystatechange = function() {
    if (request.readyState == 4 && request.status == 200) {
      // enable clicking after relay action finished
      activateClick();
    }
  }
 
  request.open('GET', '/door?id='+id, true);
  request.send();

}

function onCameraClicked(obj, id) {

  // disable further clicking until camera action finished
  deActivateClick();

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
  // clear message after 2 seconds
  clearResponseText(textid, 2000);
  
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

    // enable clicking after relay action finished
    activateClick();

    }
  }

  request.open('GET', '/cam?id='+id, true);
  request.send();
}

function clearResponseText(id, delay) {
  setTimeout(function() {
      document.getElementById(id).innerHTML = ' '
  }, delay);
}

// disable clicking
function deActivateClick() {
  document.getElementById('pedestrian').style.pointerEvents = 'none';
  document.getElementById('gate').style.pointerEvents = 'none';
  document.getElementById('l-cam').style.pointerEvents = 'none';
  document.getElementById('m-cam').style.pointerEvents = 'none';
  document.getElementById('r-cam').style.pointerEvents = 'none';    
}

// enable clicking
function activateClick() {
  document.getElementById('pedestrian').style.pointerEvents = 'auto';
  document.getElementById('gate').style.pointerEvents = 'auto';
  document.getElementById('l-cam').style.pointerEvents = 'auto';
  document.getElementById('m-cam').style.pointerEvents = 'auto';
  document.getElementById('r-cam').style.pointerEvents = 'auto';    
}