import urllib2
import json
import pprint
import time
from HTMLParser import HTMLParser

pp = pprint.PrettyPrinter(indent=4)
scrape_counter = 0

drugs = []
drug = {}
row_count = 0

all_drugs = {}

class DrugParser(HTMLParser):
  main_table_count = 0
  found_table = False
  found_row = False
  printthis = False
  row_begin = False
  col_count = 0
  #def __init__(self):
  #  self.foo = "bar"
  def handle_starttag(self, tag, attrs):
    global drug
    if DrugParser.found_table and tag == "tr":
      DrugParser.printthis = True
      DrugParser.row_begin = True
      DrugParser.col_count = 0
      drug = {}
    if len(attrs) == 2:
      if attrs[0][0] == 'width' and attrs[1][1] == 'webcasttable':
          #print "something"
          DrugParser.found_table = True

  def handle_endtag(self, tag):
    global drugs
    global drug
    global row_count
    if DrugParser.found_table and tag == "table":
          DrugParser.found_table = False
          DrugParser.printthis = False
    if DrugParser.found_table and DrugParser.row_begin and tag == "tr":
      DrugParser.row_begin = False
      row_count += 1
      if row_count > 0:
        drugs.append(drug)
      #print drug
      
  def handle_data(self, data):
    global drug
    if DrugParser.row_begin:
      if DrugParser.col_count == 1:
        drug["id"] = row_count
      if DrugParser.col_count == 3:
        drug["quantity"] = data.strip()
      if DrugParser.col_count == 5:
        drug["brand_price"] = data.strip()
      if DrugParser.col_count == 7:
        drug["brand_price_asof"] = data.strip()
      if DrugParser.col_count == 9:
        drug["generic_price"] = data.strip()
      if DrugParser.col_count == 11:
        drug["generic_price_asof"] = data.strip()

      DrugParser.col_count += 1

with open("namesandids.json", "r") as f:
  all_pharmacies = json.loads(f.read())

for pharmacy in all_pharmacies:
  time.sleep(1)
  pharma_id = pharmacy["id"] 
  drugurl = "https://apps.health.ny.gov/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=" + pharma_id + "&calledFrom=searchPharmacy"
  data = urllib2.urlopen(drugurl)

  drugs = []
  drug = {}
  row_count = 0
  parser = DrugParser()
  parser.feed(data.read())
  scrape_counter += 1
  print scrape_counter
  all_drugs[pharma_id] = drugs

with open("all_drugs.json", "w") as f:
  json.dump(all_drugs, f, indent = 4)