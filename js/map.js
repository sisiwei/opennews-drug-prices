$(document).ready(function(){

  setupMap();
  createDropdown();
  
  
})

var alldrugdata, pharmacies, map, infowindow;

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
  map = new google.maps.Map(document.getElementById("map"), mapOptions);
  infowindow = new google.maps.InfoWindow();
  pharmacies = { };
  $.getJSON("js/namesandids.json", function(data){
    for(var p=0;p<data.length;p++){
      var mark = new google.maps.Circle({
        center: new google.maps.LatLng( data[p].lat * 1.0, data[p].lng * 1.0 ),
        radius: 50,
        map: map,
        fillOpacity: 0,
        strokeOpacity: 0,
        clickable: false
      });
      pharmacies[ data[p].id ] = {
        data: data[p],
        marker: mark
      };
    }
    $.getJSON("js/all_drugs_clean.json", function(data){
      alldrugdata = data;
      setDrugMap("4");
    });
  });
}

function parsePrice(price){
  if(!price){
    return price;
  }
  return price.replace("$","").replace(",","") * 1.0;
}

function setDrugMap(code){
  if(!alldrugdata){
    // doesn't work until drug data is fully loaded
    return;
  }
  // clear old markers
  for(id in pharmacies){
    pharmacies[id].marker.setOptions({
      fillOpacity: 0,
      strokeOpacity: 0,
      clickable: false
    });
  }
  
  var pricedata = alldrugdata[ code ];
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
      strokeOpacity: 0.7,
      clickable: true
    });
  }
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
    $('#drug-drop-down').on('change', function(e){
      setDrugMap( $('#drug-drop-down').val() );
    });
  });
}

function calculateDeviations(array){
  var array = [2, 3, 4, 6, 2, 5, 7, 2, 4, 5];
  var within_std_of = 1;

  function calculate(a) {
    var r = {mean: 0, variance: 0, deviation: 0}, t = a.length;
    for(var m, s = 0, l = t; l--; s += a[l]);
    for(m = r.mean = s / t, l = t, s = 0; l--; s += Math.pow(a[l] - m, 2));
    return r.deviation = Math.sqrt(r.variance = s / t), r;
  }

  var summary = calculate(array);
  createBuckets(summary, 4);
      
  var color = [];

  function createBuckets(summary, deviations){
    var mean = summary.mean,
        deviation = summary.deviation;

    for(i=0; i<deviations; i++) {

      
    }




  }


}