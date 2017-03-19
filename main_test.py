import places
results = None

def get_place(query,type_query):
    try:
        results = places.get_name_places(query,type_query)
        return results
    except Exception:
        return "That Place Doesn't Exist Dumbshit!"

def get_place(query):
    return get_place(query,"Attractions")


results = get_place("hhfhhfdshshshs","jkjjbfjbjhbjdssd")
location_map = dict()

def get_names(num):
    if type(results) is str:
        return results
    output = ""
    if num > len(results):
        num = len(results)
    for place in results[:num]:
        location_map[place.name] = place
        output+= place.name.encode("utf-8") +"\n"
    return output

#print results
#print location_map.keys()
#location_map[u'Willis Tower'].get_details()
#print location_map[u'Willis Tower'].rating

#housing
#location
#transportation
#activites
