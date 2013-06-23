$(document).ready(function(){

  setupMap();
  createDropdown();

  $('input[name=drug_type]').change( function() {
      setDrugMap( $('#drug-drop-down').val() );
  });
  /*
  var array = [2, 3, 4, 6, 2, 5, 7, 2, 4, 5];
  var colorize = calculateDeviations(array, 4)
  for(i=0; i<array.length; i++) {
    //console.log(colorize(array[i]));
  }
  */

})

var alldrugdata, pharmacies, map, infowindow, minInfo, maxInfo, histogramData;

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
  // add MapBox tiles
  var osmMapLayer = new google.maps.ImageMapType({
    getTileUrl: function(coord, zoom) {
      return "http://c.tiles.mapbox.com/v3/examples.map-szwdot65/" + zoom + "/" + coord.x + "/" + coord.y + ".png";
	},
	tileSize: new google.maps.Size(256, 256),
	isPng: true,
	alt: "MapBox",
	name: "MapBox",
	maxZoom: 19
  });
  map.mapTypes.set('MapBox',osmMapLayer);
  map.setMapTypeId( 'MapBox' );

  infowindow = new google.maps.InfoWindow();
  minInfo = new google.maps.InfoWindow();
  maxInfo = new google.maps.InfoWindow();
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
    setDrugMap("4");
  });
}

function parsePrice(price){
  if(!price){
    return price;
  }
  return price.replace("$","").replace(",","") * 1.0;
}

function setDrugMap(code){
  // clear old markers and information
  infowindow.close();
  maxInfo.close();
  minInfo.close();
  for(id in pharmacies){
    pharmacies[id].marker.setOptions({
      fillOpacity: 0,
      strokeOpacity: 0,
      clickable: false
    });
  }

  var isBrandPrice = ($('input[name=drug_type]:checked', '#drug_type').val() == "brand_price");

  $.getJSON("js/drug/drug" + code + ".json", function (json) {

    var prices = [];
    var price_raw = [];

    var drugmin = null;
    var drugmax = null;
    
    for (var i = 0; i < json.length; i++) {
      var pharma_dict = json[i];
      if (isBrandPrice && pharma_dict.price) {
        prices.push(pharma_dict);
        price_raw.push(parsePrice(pharma_dict.price));
        if(!drugmin || parsePrice(pharma_dict.price) < drugmin.price){
          drugmin = {
            pharmacy: pharmacies[ pharma_dict.p_id + "" ],
            price: parsePrice(pharma_dict.price),
            printPrice: pharma_dict.price
          };
        }
        if(!drugmax || parsePrice(pharma_dict.price) > drugmax.price){
          drugmax = {
            pharmacy: pharmacies[ pharma_dict.p_id + "" ],
            price: parsePrice(pharma_dict.price),
            printPrice: pharma_dict.price
          };
        }
        
      } else if (!isBrandPrice && pharma_dict.g_price){
        prices.push(pharma_dict);
        price_raw.push(parsePrice(pharma_dict.g_price));
        if(!drugmin || parsePrice(pharma_dict.g_price) < drugmin.price){
          drugmin = {
            pharmacy: pharmacies[ pharma_dict.p_id + "" ],
            price: parsePrice(pharma_dict.g_price),
            printPrice: pharma_dict.g_price
          };
        }
        if(!drugmax || parsePrice(pharma_dict.g_price) > drugmax.price){
          drugmax = {
            pharmacy: pharmacies[ pharma_dict.p_id + "" ],
            price: parsePrice(pharma_dict.g_price),
            printPrice: pharma_dict.g_price
          };
        }
      }
    }
    
    var extra; 
    if (isBrandPrice){
      extra = "Brand ";
    } else {
      extra = "Generic ";
    }

    minInfo.setContent("<h4 class='lowest'>LOWEST</h4><h3>" + drugmin.pharmacy.data.name + "</h3><p>" + drugmin.pharmacy.data.phone + "</p><p class='price'>" + extra + "Price: <strong>" + drugmin.printPrice + "</strong></p><p class='data-link'><a target='_blank' href='https://apps.health.ny.gov/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=" + drugmin.pharmacy.data.id + "&calledFrom=searchPharmacy'>Price data from NYDOH</a></p>");
    minInfo.setPosition(drugmin.pharmacy.marker.getCenter());
    minInfo.open(map);

    maxInfo.setContent("<h4 class='highest'>HIGHEST</h4><h3>" + drugmax.pharmacy.data.name + "</h3><p>" + drugmax.pharmacy.data.phone + "</p><p class='price'>" + extra + "Price: <strong>" + drugmax.printPrice + "</strong></p><p class='data-link'><a target='_blank' href='https://apps.health.ny.gov/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=" + drugmax.pharmacy.data.id + "&calledFrom=searchPharmacy'>Price data from NYDOH</a></p>");
    maxInfo.setPosition(drugmax.pharmacy.marker.getCenter());
    maxInfo.open(map);

    var colorize = calculateDeviations(price_raw, 4);
    for (var i = 0; i < prices.length; i++) {
      bindClick( pharmacies[ prices[i].p_id + "" ], prices[i] );
      //console.log(colorize(price_raw[i]));
      pharmacies[ prices[i].p_id + "" ].marker.setOptions({
        fillColor: "#" + colorize(price_raw[i]),
        strokeColor: "#" + colorize(price_raw[i]),
        fillOpacity: 0.7,
        strokeOpacity: 0.7,
        clickable: true
      });
    }
    
    /*

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
    */

  });

  
}

function bindClick(pharmacy, prices){
  google.maps.event.clearInstanceListeners(pharmacy.marker);
  google.maps.event.addListener(pharmacy.marker, 'click', function(e){
    var content = '';
    if(pharmacy.data.name){
      content += '<h3>' + pharmacy.data.name + '</h3><p>' + pharmacy.data.phone + '</p>';
    }
    if(prices.price){
      content += '<strong>Brand Price</strong>: ' + prices.price;
    }
    if(prices.g_price){
      content += '<strong>Generic</strong>: ' + prices.g_price;
    }
    infowindow.setContent(content);
    infowindow.setPosition( pharmacy.marker.getCenter() );
    infowindow.open(map);
    maxInfo.close();
    minInfo.close();
  });
}

function createDropdown(){
  $.getJSON("js/drug-list.json", function(data){
    var htmlDump = [];
    $.each(data, function(k,v){
      if (k == 3){
        htmlDump.push("<option value='" + v.id + "' selected>" + v.drugName + "</option>");
      } else {
        htmlDump.push("<option value='" + v.id + "'>" + v.drugName + "</option>");
      }
    })
    $('#drug-drop-down').html(htmlDump.join(''));
    $('#drug-drop-down').on('change', function(e){
      setDrugMap( $('#drug-drop-down').val() );
    });
  });
}

function calculateDeviations(array, deviations){
  function calculate(a) {
    var r = {mean: 0, variance: 0, deviation: 0}, t = a.length;
    for(var m, s = 0, l = t; l--; s += a[l]);
    for(m = r.mean = s / t, l = t, s = 0; l--; s += Math.pow(a[l] - m, 2));
    return r.deviation = Math.sqrt(r.variance = s / t), r;
  }

  var summary = calculate(array);
      
  createBuckets = function(summary, deviations){
    var colorArray = ["FFF5F0","FEE0D2","FCBBA1","FC9272","FB6A4A","EF3B2C","CB181D","99000D"];

    var mean = summary.mean,
        deviation = summary.deviation,
        allBuckets = [];

    for(i=0; i<deviations; i++) {
      var minusDev = {};
      minusDev.min = mean - deviation * (i+1);
      minusDev.max = mean - deviation * i;
      minusDev.color = colorArray[3-i];
      minusDev.count = 0
      allBuckets.push(minusDev);

      var addDev = {};
      addDev.min = mean + deviation * i;
      addDev.max = mean + deviation * (i+1);
      addDev.color = colorArray[4+i];
      addDev.count = 0;
      allBuckets.push(addDev);

      if (i == deviations-1){
        var lastMinusDev = {};
        lastMinusDev.min = -9999;
        lastMinusDev.max = minusDev.min;
        lastMinusDev.color = minusDev.color
        lastMinusDev.count = 0
        allBuckets.push(lastMinusDev);

        var lastAddDev = {};
        lastAddDev.min = addDev.max;
        lastAddDev.max = 10000000000;
        lastAddDev.color = addDev.color;
        lastAddDev.count = 0;
        allBuckets.push(lastAddDev);
      }
    }

    // For each number in the array...
    $.each(array, function(k,v){
      // ...go through each bucket to categorize it, for the histogram.
      $.each(allBuckets, function(key, val){
        if (v < val.max && v >= val.min){
          val.count++;
        }
      })
    })

    histogramData = allBuckets;

    return function(num){
      var selectedColor = "";
      $.each(allBuckets, function(k,v){
        if (num < v.max && num >= v.min){
          selectedColor = v.color;
        }
      })
      return selectedColor;
    };
  }

  return createBuckets(summary, deviations);
}
