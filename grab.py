import io
import os
import json

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

dir = os.path.abspath(__file__ + '/../')
output = os.path.join(dir, 'restaurants.json')

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
response_2 = client.search("Convoy Street, San Diego, CA 92111", **params_2)

with open(output, 'w') as out:
  out.write('[')
  convoy = dict()
  convoy['isExpandable'] = True
  convoy['isExpanded'] = False
  convoy['isVisible'] = True
  convoy['label'] = 'Convoy'
  convoy['checked'] = 1
  convoy['cellIdentifier'] = 'idCategoryCell'
  convoy['additionalRows'] = 40
  json.dump(convoy, out)
  out.write(',')
  out.write('\n')

  for i in range(0, 20):
    dic = dict()
    dic['isExpandable'] = False
    dic['isExpanded'] = False
    dic['isVisible'] = False
    dic['label'] = response.businesses[i].name
    dic['png'] = response.businesses[i].image_url
    dic['checked'] = True
    dic['cellIdentifier'] = 'idItemCell'
    dic['additionalRows'] = 0
    json.dump(dic, out)
    out.write(',')
    out.write('\n')

  for i in range(0, 20):
    dic = dict()
    dic['isExpandable'] = False
    dic['isExpanded'] = False
    dic['isVisible'] = False
    dic['label'] = response_2.businesses[i].name
    dic['png'] = response_2.businesses[i].image_url
    dic['checked'] = True
    dic['cellIdentifier'] = 'idItemCell'
    dic['additionalRows'] = 0
    json.dump(dic, out)
    if i != 19:
      out.write(',')
    out.write('\n')
  
  out.write(']')