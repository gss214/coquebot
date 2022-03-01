from time import sleep
import os
import tweepy

class coqueBot():
    def __init__(self) -> None:
        self.api_key = str(os.environ.get('API_KEY'))
        self.api_secret_key = str(os.environ.get('API_SECRET_KEY'))
        self.access_token = str(os.environ.get('ACCESS_TOKEN'))
        self.access_token_secret = str(os.environ.get('ACESS_TOKEN_SECRET'))
        print(self.access_token)
        print(self.access_token_secret)
        #bearer_token = str(os.environ.get('BEARER_TOKEN'))

        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)
        
        try:
            self.api.verify_credentials()
            print("Authentication OK")
            self.run()
        except:
            print("Error during authentication")

    def fav_retweet_coque(self):
        tweets = self.api.search_tweets(q='from:@coqueluchismo')
        for tweet in tweets:
            try:
                if not tweet.text.startswith('RT'):
                    self.api.retweet(tweet.id)
                    print(f'Coque bot retweetou: {tweet.text}')
            except Exception as e:
                pass

    def run(self):
        while True:
            self.fav_retweet_coque()
            sleep(15)
            
if __name__ == '__main__':
    coquebot = coqueBot()