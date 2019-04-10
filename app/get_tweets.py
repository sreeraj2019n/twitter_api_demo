#fetch tweets for a partiular query from twitter using twitter API
import twitter
from app import app
api = twitter.Api(consumer_key=app.config['CONSUMER_KEY'],
                      consumer_secret=app.config['CONSUMER_SECRET'],
                      access_token_key=app.config['ACCESS_TOKEN_KEY'],
                      access_token_secret=app.config['ACCESS_TOKEN_SECRET'])


class getTweets(object):
    def getRecentTweets(self,searchTerm):
        try:
            publicTweets = api.GetSearch(raw_query="q="+ searchTerm.lower() + "%20&result_type=recent&count=30")
        except Exception as err:
            print(err)
            return []
        else:       
            return publicTweets

class getUserTimeline(object):
    def getLatestTimeline(self,screen_name):
        try:
            timeline =  api.GetUserTimeline(screen_name = screen_name)
        except Exception as err:
            print(err)
            return []
        else:       
            return timeline
