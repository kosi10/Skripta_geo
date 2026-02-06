import json
from geopy.distance import geodesic

with open("json/pois.geojson", "r") as f:
    file1 = json.load(f)

with open("json/wikidata_slovenia.json", "r", encoding="utf-8") as f:
    file2 = json.load(f)
    match=[]
    combined = []
    #counter = 0
    for item in file1["features"]:
        cord1 = item["geometry"]["coordinates"]

        min = 100000000000000
        min_item = []

        for item2 in file2:
            cordtemp = item2["coord"][6:-1]
            try:
                cord2 = list(
                    map(float, cordtemp.replace("Point(", "").replace(")", "").split())
                )
            except ValueError:
                continue
            distance_m = geodesic((cord1[0], cord1[1]), (cord2[0], cord2[1])).m
            
            if(min > distance_m):
                min = distance_m
                min_item = item2

        #print(min," m")
        #print(min_item)
        min_d = str(min) + " m"
        match = {
            "pois": item,
            "slo": min_item,
            "dist": min_d
        }
        combined.append(match)

        '''
        counter += 1
        if counter == 30:     
             break
        '''

    #print(combined)
    with open("json/combined.json", "w", encoding="utf-8") as f:
            json.dump(combined, f, indent=2, ensure_ascii=False)
