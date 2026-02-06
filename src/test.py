from geopy.distance import geodesic

distance_m = geodesic((14.3769973, 46.2729863), (13.7513986, 46.5177272)).km
print(distance_m," km")