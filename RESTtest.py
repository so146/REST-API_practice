import json, requests
import httplib2

import sys
import codecs

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyCoo_T8OFrZSgOUpGPntPK-wOLWKbFqD7c"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

#lat, lon = getGeocodeLocation("Tokyo, Japan")
#print(lat, lon)

"""
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='WUN5NHHMMWWUHYWCWQD2H1YATO3SHG552XYKJF1CPHWMU2KV',
  client_secret='F2BAWL0NH40O52AXDTN5TW31X5JSKDCXXNOVWKNC2ZC2FRNP',
  v='20170801',
  ll='37.392971,-122.076044',
  query='Pizza',
  limit=2
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

out = data['response']['groups'][0]['items']#[0]['venue']['location']
print(len(out))
#print(out)

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
"""
foursquare_client_id = "WUN5NHHMMWWUHYWCWQD2H1YATO3SHG552XYKJF1CPHWMU2KV"
foursquare_client_secret = "F2BAWL0NH40O52AXDTN5TW31X5JSKDCXXNOVWKNC2ZC2FRNP"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	lat, lon = getGeocodeLocation(location)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s'% (foursquare_client_id, foursquare_client_secret, lat, lon, mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	print(result)
	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
	