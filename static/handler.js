//
// handler functions for button click events
//

function mouse_down_pe() {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", "/mouse_down_pe", true);
  xmlhttp.send();
}

function mouse_down_eg() {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", "/mouse_down_eg", true);
  xmlhttp.send();
}

// add event listener to tuerl button
var el1 = document.getElementById("pedestrian");
el1.addEventListener("mousedown", mouse_down_pe, false);
// el1.addEventListener("mouseup", mouse_up_pe, false);

// add event listener to tor button
var el2 = document.getElementById("gate");
el2.addEventListener("mousedown", mouse_down_eg, false);
// el2.addEventListener("mouseup", mouse_up_eg, false);

