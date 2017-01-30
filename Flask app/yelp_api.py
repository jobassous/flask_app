from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
	auth = Oauth1Authenticator(
    	consumer_key=os.environ['yelp_consumer_key'],
    	consumer_secret=os.environ['yelp_consumer_secret'],
    	token=os.environ['yelp_token'],
    	token_secret=os.environ['yelp_token_secret']
	)

	client = Client(auth)
	
	params = {
    	'term': term,
    	'lang': 'en',
    	'limit': 3
	}

	response = client.search(location, **params)

	for business in response.businesses:
		print(business.name)

get_businesses('New York City', 'Kosher food')