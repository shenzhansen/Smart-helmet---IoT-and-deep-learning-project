function initMap() {
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var directionsService = new google.maps.DirectionsService;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: {lat: 41.85, lng: -87.65}
  });
  directionsDisplay.setMap(map);
  directionsDisplay.setPanel(document.getElementById('right-panel'));

  var control = document.getElementById('floating-panel');
  control.style.display = 'block';
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);

  var onChangeHandler = function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
  };
  calculateAndDisplayRoute(directionsService, directionsDisplay);
  document.getElementById('start').addEventListener('change', onChangeHandler);
  document.getElementById('end').addEventListener('change', onChangeHandler);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
  var start = document.getElementById('start').value;
  var end = document.getElementById('end').value;
  directionsService.route({
    origin: start,
    destination: end,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}
function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}
var destination = getUrlVars()["destination"];
document.getElementById('end').value = destination;
document.getElementById("left-corner").onclick = function () { };
function leftFunction(){
  var Ip = new URL("http://129.236.236.197:1500");

  params = {state:'end', destination:String(document.getElementById('end').value)};
  Object.keys(params).forEach(key => Ip.searchParams.append(key, params[key]));
  fetch(Ip)
  .then(data=>{return data.json()})
  .then(res=>{console.log(res);})
  .catch(error=>{console.log(error);})
  window.location.href = "http://guosl.com/iot";
}
document.getElementById("right-corner").onclick = function () { };

function rightFunction(){
  const Url = 'https://jsonplaceholder.typicode.com/posts';
  const Wea_url = 'http://api.openweathermap.org/data/2.5/weather?lat=40.7975&lon=-73.9676&units=imperial&appid=e7477656acbae304123ccb133b647055';
  var Ip = new URL("http://129.236.236.197:1500");

  params = {state:'start', destination:String(document.getElementById('end').value)};
  Object.keys(params).forEach(key => Ip.searchParams.append(key, params[key]));
  fetch(Ip)
  .then(data=>{return data.json()})
  .then(res=>{console.log(res);})
  .catch(error=>{console.log(error);})
}
