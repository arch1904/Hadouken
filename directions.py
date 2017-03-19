import googlemaps
from datetime import datetime
import config

gmaps = googlemaps.Client(key=config.google_key)

def get_directions(current_location,destination):

    # Geocoding an address
    #geocode_result = gmaps.geocode(current_location)

    # Look up an address with reverse geocoding
    #reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="driving",
                                         departure_time=now)
    return directions_result

print get_directions("ff","gg")
