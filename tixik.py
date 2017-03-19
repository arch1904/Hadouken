import geocode
import urllib2



def get_places(location):
	tixik_api_key = config.tixik_api_key
	language = "en"
	coords = geocode.get_coords(location)
	limit = 20
	latitude = coords[0]
	longitude = coords[1]
	tixik_request_url = "http://www.tixikcom/{0}/api/nearby/?lat={1}&lng={2}&limit={3}&key={4}".format(language,latitude,longitude,limit,tixik_api_key)
	print tixik_request_url
	response = urllib2.urlopen(tixik_request_url)
	data = json.load(response)   
	print data


	

get_places("Champaign")





