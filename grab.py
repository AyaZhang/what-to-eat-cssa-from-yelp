"""
TODO:
1. Convoy: Szechuan
  - restaurant
  - restaurant
  - restaurant
  - ... x 10
2. Convoy: Dim Sum
  - restaurant
  - restaurant
  - restaurant
  - ... x 10
"""

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
  "limit": 10,
  "category_filter": "szechuan"
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_2 = {
  "term": "Restaurants",
  "sort": 2,
  "limit": 10,
  "category_filter": "cantonese"
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_3 = {
  "term": "Restaurants",
  "sort": 2,
  "limit": 10,
  "category_filter": "dimsum"
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_4 = {
  "term": "Restaurants",
  "sort": 2,
  "limit": 10,
  "category_filter": "taiwanese"
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_5 = {
  "term": "Restaurants",
  "sort": 2,
  "limit": 10,
  "category_filter": "korean"
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_6 = {
  "term": "Restaurants",
  "sort": 2,
  "limit": 10,
  "category_filter": "japanese"
  #"location": "Convoy Street, San Diego, CA 92111"
}

params_7 = {
  "term": "Restaurants",
  "sort": 2,
  "limit": 10,
  "category_filter": "chinese"
  #"location": "Convoy Street, San Diego, CA 92111"
}

response = client.search("Convoy Street, San Diego, CA 92111", **params_7)
response_2 = client.search("Convoy Street, San Diego, CA 92111", **params_2)
for i in range(0, len(response.businesses)):
  print(response.businesses[i].name)

"""
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
  """