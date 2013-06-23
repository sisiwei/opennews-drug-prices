$(document).ready(function(){

  setupMap();
  createDropdown();
  
  
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
  $.getJSON("js/drug-list.json", function(data){
    var htmlDump = [];
    $.each(data, function(k,v){
      htmlDump.push("<option value='" + v.id + "'>" + v.drugName + "</option>");
    })
    $('#drug-drop-down').html(htmlDump.join(''));
  });
}