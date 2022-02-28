from time import sleep
import tweepy


api_key = '10ZJkrP9fGSO8UC2cNYRII440'
api_secret_key = 'TDAociKwrPlTd1N5xYIOsjo7OuglikV9V4bc8NeXGtH0lGIINB'
access_token = '1497819855508189201-Qda53dd4zHQugTt5bgp3kjNIEzI6tS'
access_token_secret = 'CcsirWJ410MK62a6mUlxofdkXxbOLqz8Nv4FVNoOoy5pg'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGu9ZgEAAAAAXeUkYtbWXSEgaQAZZzQUC6sYw1g%3DSDyRqiB5JBuZGvUR9Opyw1fXWGs7mi5hrXTZkx745IzUfZPCG2'

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
            pass

while True:
    fav_retweet_coque()
    sleep(15)
    