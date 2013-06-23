# scrapegeo.py
# combine a CSV from scrapezip.py and the KML output from Fusion Tables

import json

nyc_csv = open('nyc-pharmacies.csv','r')

pharmacies = { }
if(1==1):
  while(True):
    csvline = nyc_csv.readline()
    if(csvline.find(',') == -1):
      break
    id = csvline.split('","')[0].replace('"','')
    
    pharmacy = {
      "id": id,
      "name": csvline.split('","')[1],
      "address": csvline.split('","')[2],
      "zip": csvline.split('","')[3],
      "phone": csvline.split('","')[4].replace('"','')
    }
    
    pharmacies[ id ] = pharmacy

nyc_kml = open('nyc-pharmacies.kml','r')

indescription = 0
incoordinates = 0
inid = 0

if(1==1):
  while(True):
    kmlline = nyc_kml.readline()
    if(kmlline.find('</kml>') > -1):
      break

    if(kmlline.find('<description>') > -1):
      indescription = 1
    if(indescription == 1):
      if(kmlline.find('ID:</b>') > -1):
        # <b>ID:</b> 28943<br>
        inid = kmlline[ kmlline.find('</b> ') + 5: kmlline.find('<br>') ]
      
      if(kmlline.find('</description>') > -1):
        indescription = 0

    if(kmlline.find('<Point>') > -1):
      incoordinates = 1
    if(incoordinates == 1):
      if(kmlline.find('<coordinates>') > -1):
        coords = kmlline.split(',')
        lng = coords[0]
        lng = lng[ lng.find('>') + 1 : ]
        lat = coords[1]
        
        pharmacies[inid]["lat"] = float(lat)
        pharmacies[inid]["lng"] = float(lng)
                
        #pharmacies[ inid ].append(lat)
        #pharmacies[ inid ].append(lng)
      
    
      if(kmlline.find('</Point>') > -1):
        incoordinates = 0

output = "json"

if(output == "csv"):
  print '"ID","Name","Address","Zip","Phone","lat","lng"'
  for id in pharmacies:
    if(pharmacies[id].has_key("lng") == False):
      continue

    p = [ ]
    p.append(id)
    p.append( pharmacies[id]["name"] )
    p.append( pharmacies[id]["address"] )
    p.append( pharmacies[id]["zip"] )
    p.append( pharmacies[id]["phone"] )
    p.append( pharmacies[id]["lat"] )
    p.append( pharmacies[id]["lng"] )
  done = 1
elif(output == "json"):
  plist = [ ]
  for id in pharmacies:
    plist.append( pharmacies[id] )
  print json.dumps( plist )
elif(output == "geojson"):

  geojson = {
    "type": "FeatureCollection",
    "features": [ ]
  }
  for id in pharmacies:
    pharmacy = pharmacies[id]
    if(pharmacy.has_key("lng") == False):
      continue
    
    geojson["features"].append({
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [ pharmacy["lng"], pharmacy["lat"] ]
  },
  "properties": {
    "id": pharmacy["id"].replace("\n",""),
    "name": pharmacy["name"].replace("\n",""),
    "address": pharmacy["address"].replace("\n",""),
    "zip": pharmacy["zip"].replace("\n",""),
    "phone": pharmacy["phone"].replace("\n","")
  }
})

  print json.dumps( geojson )