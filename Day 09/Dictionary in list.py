#Dictionary in list

#Day 09

#sumith sai koraboina

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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(name,no_of_visits,visited_places):
    new_country={}
    new_country["country"]=name
    new_country["visits"]=no_of_visits
    new_country["cities"]=visited_places
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
