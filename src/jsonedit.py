import json

with open("json/wikidata_slovenia.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("json/wiki_slo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)