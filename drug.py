import urllib2
import json
import pprint
from HTMLParser import HTMLParser

pp = pprint.PrettyPrinter(indent=4)

drugs = []
drug = {}
row_count = 0

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
          print "something"
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
      print drug
      
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

    
drugurl = "https://apps.health.ny.gov/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19404&calledFrom=searchPharmacy"
data = urllib2.urlopen(drugurl)

parser = DrugParser()
parser.feed(data.read())

with open("drug.json", "w") as f:
  json.dump(drugs, f)



