import io
import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# read API keys
with io.open('config_secret.json') as cred:
  creds = json.load(cred)
  auth = Oauth1Authenticator(**creds)
  client = Client(auth)

client = Client(auth)

params = {
  "term": "Restaurants",
  "sort": 2,
  "category_filter": "chinese",
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_2 = {
  "term": "Restaurants",
  "sort": 2,
  "offset": 20,
  "limit": 20,
  "category_filter": "chinese",
  #"location": "Convoy Street, San Diego, CA 92111"
}

response = client.search("Convoy Street, San Diego, CA 92111", **params)
for i in range(0, len(response.businesses)):
  print(response.businesses[i].name)

response_2 = client.search("Convoy Street, San Diego, CA 92111", **params_2)
for i in range(0, len(response_2.businesses)):
  print(response_2.businesses[i].name)