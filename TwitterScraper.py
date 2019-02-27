from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#These key are my Twitter dev API keys, so I have blanked mine out
consumer_key = '#########'
consumer_secret = '#########'
access_token = '##############'
access_secret = '#############'

print('Hey! Welcome to my twitter data scraper!')
variant = str(input("Please enter a hashtag you would like me to scrape: "))
print('Collecting Data...')

class LiveTweets(StreamListener):
  
    #this function writes the data to a json file
    def on_data(self, data):
        with open(variant+'.json', 'a') as f:
            f.write(data)
            return True
    
    #Will output error if there is one
    def on_error(self, status):
            print(status)
            return True

if __name__ == "__main__":

    liveTweets = LiveTweets()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, liveTweets)
    
    
    stream.filter(track=[variant])
