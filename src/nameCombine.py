import json
from geopy.distance import geodesic
from difflib import get_close_matches

with open("json/pois.geojson", "r") as f:
    file1 = json.load(f)

with open("json/wiki_slo.json", "r", encoding="utf-8") as f:
    file2 = json.load(f)

with open("json/nameCombine.json", "r", encoding="utf-8") as f:
    file3 = json.load(f)

combined = []
print(len(file1["features"]))
print(len(file3))
print(len(file2))
#counter = 0
nameMatches = []
for item, match in zip(file1["features"], file3):
    name1 = item["properties"]["name"]

    target = str(match)[2:-2]

    find = next(
        (d for d in file2 if d["itemLabel"] == target),
        None
    )

    combine = {
            "pois": item,
            "slo": find,
        }
    combined.append(combine)


with open("json/combinedNames.json", "w", encoding="utf-8") as f:
            json.dump(combined, f, indent=2, ensure_ascii=False)
