from mapbox import Geocoder
import os
import config
def get_coords(location):
	mapbox_api_key = config.mapbox_key
	geocoder = Geocoder(access_token = mapbox_api_key)
	response = geocoder.forward(location).json()
	center = response[u'features'][0][u'center']
	coords = (center [0],center [1])
	return coords



