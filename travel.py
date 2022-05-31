travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    x = { "country" : country, "visits": visits}
    city_foo = []
    for city in cities:
        city_foo.append(city)
    x.update({"cities": city_foo})
    travel_log.append(x)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)