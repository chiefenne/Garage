//
// handler function for button click events
//

function onButtonClicked(obj, id) {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', '/click?id=' + id, true);
  xmlhttp.send();
};
