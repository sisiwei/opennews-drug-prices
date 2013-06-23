$(document).ready(function(){

  setupMap();
  createDropdown();
  
  
})

var alldrugdata;

function setupMap(){
  google.maps.visualRefresh=true;
  var mapOptions = {
    center: new google.maps.LatLng(40.78343, -73.96624),
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    streetViewControl: false,
    zoomControlOptions: {
        position: google.maps.ControlPosition.TOP_RIGHT
    },
    panControlOptions: {
        position: google.maps.ControlPosition.TOP_RIGHT
    }
  };
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
  var infowindow = new google.maps.InfoWindow();
  var pharmacies = { };
  $.getJSON("js/namesandids.json", function(data){
    for(var p=0;p<data.length;p++){
      var mark = new google.maps.Circle({
        center: new google.maps.LatLng( data[p].lat * 1.0, data[p].lng * 1.0 ),
        radius: 50,
        map: map,
        fillOpacity: 0,
        strokeOpacity: 0
      });
      pharmacies[ data[p].id ] = {
        data: data[p],
        marker: mark
      };
    }
    var parsePrice = function(price){
      if(!price){
        return price;
      }
      return price.replace("$","").replace(",","") * 1.0;
    };
    $.getJSON("js/all_drugs_clean.json", function(data){
      alldrugdata = data;
      var pricedata = alldrugdata["4"];
      var min = Math.min( parsePrice(pricedata[0].price) || parsePrice(pricedata[0].g_price), parsePrice(pricedata[0].g_price) || parsePrice(pricedata[0].price) );
      var max = Math.max( parsePrice(pricedata[0].price) || parsePrice(pricedata[0].g_price), parsePrice(pricedata[0].g_price) || parsePrice(pricedata[0].price) );
      for(var a=1;a<pricedata.length;a++){
        if(!pricedata[a].price && ! pricedata[a].g_price){
          continue;
        }
        min = Math.min(min, parsePrice(pricedata[a].price) || parsePrice(pricedata[a].g_price));
        min = Math.min(min, parsePrice(pricedata[a].g_price) || parsePrice(pricedata[a].price));
        max = Math.max(max, parsePrice(pricedata[a].price) || parsePrice(pricedata[a].g_price));
        max = Math.max(max, parsePrice(pricedata[a].g_price) || parsePrice(pricedata[a].price));
      }
      for(var a=0;a<pricedata.length;a++){
        var id = pricedata[a].p_id;
        var mymin = parsePrice(pricedata[a].g_price) || parsePrice(pricedata[a].price);
        mymin = Math.min(mymin, parsePrice(pricedata[a].price) || parsePrice(pricedata[a].g_price));
        var rvalue = Math.floor(127 + 127 * (Math.log(mymin) - Math.log(min)) / ( Math.log(max) - Math.log(min) ));
        bindClick( pharmacies[ id + "" ], pricedata[a] );
        pharmacies[ id + "" ].marker.setOptions({
          fillColor: "rgb(" + rvalue + ",0,0)",
          strokeColor: "rgb(" + rvalue + ",0,0)",
          fillOpacity: 0.7,
          strokeOpacity: 0.7
        });
      }
    });
  });
}

function bindClick(pharmacy, prices){
  google.maps.event.addListener(pharmacy.marker, 'click', function(e){
    var content = '';
    if(pharmacy.data.name){
      content += '<h3>' + pharmacy.data.name + '</h3>';
    }
    if(prices.price){
      content += '<strong>Price</strong>: ' + prices.price;
    }
    if(prices.g_price){
      content += '<strong>Generic</strong>: ' + prices.g_price;
    }
    infowindow.setContent(content);
    infowindow.setPosition( pharmacy.marker.getCenter() );
    infowindow.open(map);
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