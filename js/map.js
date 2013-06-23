$(document).ready(function(){

  setupMap();

  
  
})

function setupMap(){
  google.maps.visualRefresh=true;
  var mapOptions = {
    center: new google.maps.LatLng(40.78343, -73.96624),
    zoom: 11,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    streetViewControl: false
  };
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
  $.getJSON("js/namesandids.json", function(data){
    for(var p=0;p<data.length;p++){
      new google.maps.Marker({
        position: new google.maps.LatLng( data[p].lat * 1.0, data[p].lng * 1.0 )
      });
    }
  });
}

function createDropdown(){



}