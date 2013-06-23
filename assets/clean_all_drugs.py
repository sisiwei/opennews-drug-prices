import json
import pprint

pp = pprint.PrettyPrinter(indent = 2)

all_drugs_clean = {}

with open("../js/all_drugs.json", "r") as f:
  pharmacies = json.loads(f.read())

with open("../js/namesandids.json", "r") as f1:
  pharmacy_ids = json.loads(f1.read())


def find_pharmacy(p_id):
  for p in pharmacy_ids:
    if str(p_id) == p["id"]:
      return p

for drug_id in range(1,151):
  drug_arr = []
  for pharma_id, array in pharmacies.iteritems():
    drug = {}
    for d in array:
      if d["id"] == drug_id: # we have found our drug
        p = find_pharmacy(pharma_id)
        drug["p_id"] = pharma_id
        if d["brand_price"] != "No Generic" and d["brand_price"] != "N/A":
          drug["price"] = d["brand_price"]
        if d["generic_price"] != "No Generic" and d["generic_price"] != "N/A":
          drug["g_price"] = d["generic_price"]
        break

    if "price" in drug or "g_price" in drug:
      drug_arr.append(drug)

  with open("../js/drug/drug{}.json".format(str(drug_id)), "w") as f:
    json.dump(drug_arr, f)

  all_drugs_clean[str(drug_id)] = drug_arr

#pp.pprint(all_drugs_clean)

with open("../js/all_drugs_clean.json", "w") as f:
  json.dump(all_drugs_clean, f)





        


  
