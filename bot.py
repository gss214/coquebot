from time import sleep
from unittest import result
import tweepy
import os

api_key = os.environ.get('API_KEY')
api_secret_key = os.environ.get('API_SECRET_KEY')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def fav_retweet_coque():
    tweets = api.search_tweets(q='from:@coqueluchismo')
    for tweet in tweets:
        try:
            if not tweet.text.startswith('RT'):
                api.retweet(tweet.id)
                print(f'Coque bot retweetou: {tweet.text}')
        except Exception as e:
            print(e)

while True:
    fav_retweet_coque()
    sleep(15)