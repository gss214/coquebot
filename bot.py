from time import sleep
import tweepy
import os

api_key = os.environ.get('API_KEY')
api_secret_key = os.environ.get('API_SECRET_KEY')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret_key, access_token=access_token, access_token_secret=access_token_secret)

def fav_retweet_coque():
    tweets = client.get_users_tweets('1471176402615648256', expansions=['author_id', 'referenced_tweets.id'])
    for tweet in tweets.data:
        if not tweet.referenced_tweets or tweet.referenced_tweets[0].data['type'] == 'quoted':
            print(tweet.text)
            try:
                client.retweet(tweet.id)
            except Exception as e:
                print(e)

while True:
    fav_retweet_coque()
    sleep(15)