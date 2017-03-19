from googleplaces import GooglePlaces, types, lang
import config

api_key = config.google_key
google_places = GooglePlaces(api_key)
def get_name_places(location, query_term):
    intended_location = location
    search_key = query_term
    radius = 20000
    #types = [types.TYPE_FOOD]

    query_result = google_places.nearby_search(
            location= intended_location, keyword= search_key,
            radius=radius)#types = type
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:
    # http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

    if query_result.has_attributions:
        print query_result.html_attributions


    for place in query_result.places[1:2]:
        # Returned places from a query are place summaries.
        #print place.name
        #print place.geo_location
        #print place.place_id

        # The following method has to make a further API call.
        #place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        #print place.details # A dict matching the JSON response from Google.
        #print place.local_phone_number
        #print place.international_phone_number
        #print place.website
        #print place.url

        # Getting place photos

        for photo in place.photos:
            # 'maxheight' or 'maxwidth' is required
            photo.get(maxheight=500, maxwidth=500)
            # MIME-type, e.g. 'image/jpeg'
            photo.mimetype
            # Image URL
            photo.url
            # Original filename (optional)
            photo.filename
            # Raw image data
            photo.data


    # Are there any additional pages of results?
    if query_result.has_next_page_token:
        query_result_next_page = google_places.nearby_search(
                pagetoken=query_result.next_page_token)
    return query_result.places
