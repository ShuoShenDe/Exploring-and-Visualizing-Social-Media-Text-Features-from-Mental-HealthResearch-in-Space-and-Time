import os
import sys
import tweepy as tw
import pandas as pd
import time
import json
import click

consumer_key = "9koCT8AsP53AlNzhdC7uJvVvR"
consumer_secret = "KsgN5Z4Pbs3fmc4EgAyVntSEaSOuUMRaFx2e7wiodRtCDpsdte"
access_token = "1395362346441265155-XmLpK0Mlclzk2AUX5lfvSFmDB8soj9"
access_token_secret = "r7krIY3YvKT0ZBVM4yrXvnBOnfZoC4gIgGIbLcMMKaW22"


def authenticate():
    auth = tw.OAuthHandler(consumer_key, consumer_secret)  # Creating the authentication object
    auth.set_access_token(access_token, access_token_secret)
    return auth

def get_api():
    auth = authenticate()
    api = tw.API(auth)  # Creating the API object while passing in auth information
    # , wait_on_rate_limit=True, wait_on_rate_limit_notify = True)
    return api

class Listener(tw.StreamListener):

    def __init__(self, file_name):
        safe_fname = click.format_filename(file_name)
        self.outfile = "stream_%s.jsonl" % safe_fname

    def on_data(self, raw_data):
        try:
            # data = json.loads(raw_data)

            # if data['coordinates'] or data['geo'] or data['place']:  # TRY TO FILTER FOR COORD/GEO
                # https://shuzhanfan.github.io/2018/03/twitter-streaming-collection/

            with open(self.outfile, 'a') as f:
                f.write(raw_data)
                return True

        except BaseException as e:
            sys.stderr.write("Error: on_data(): {}\n".format(e))
            # time.sleep(5)
        return True


if __name__ == '__main__':
    # GEO: only approx 1% of tweets// PLACE: often sarcastic/fantasy and small percentage// LOCATION: approx 50% but also ofter sarcastic/ fantasy
    # MAYBE CHANGE THIS TO SOME sys.arg// BAD CODE!
    # query = "-is:retweet place:'New York City'"  # No retweets and must be in NYC
    # query = "-is:retweet place:'New York City'&locations=-74,40,-73,41"
    # query = "place:'New York City'"
    # THIS HAS TO BE CHANGED// BAD CODE!
    query_fname = "nyc_test"
    # loc = [-74, 40, -73, 41]  # NEW YORK CITY
    loc = [-77.5, 38.5, -76.7, 39.1] # W.DC
    # https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters

    auth = authenticate()
    twitter_stream = tw.Stream(auth, Listener(query_fname))
    # twitter_stream.filter(track=query)
    twitter_stream.filter(locations=loc, is_async=True)
    # twitter_stream.filter(track=query, locations=loc, languages=["en"], is_async=True)

    '''
    # THIS DOES NOT SAVE JSON BUT INSTEAD FILTER AND WRITE IN pd.df AND SAVE AS CSV
    
    tweetCount = 3  # Limited to three for testing purposes
    language = "en"  # Language code (follows ISO 639-1 standards)
    geo = 1234  # Need LatLon here
    # date_since = "2021-01-01"

    results = api.search(q=query, lang=language, count=tweetCount)  # Calling the user_timeline function with parameters
    # geocode=geo

    data = [[tweet.user.screen_name, tweet.user.location, tweet.text, tweet.place, tweet.coordinates] for tweet in
            results]  # Wanted data
    df = pd.DataFrame(data=data, columns=['user', 'home', 'text', 'place', 'coordinates'])  # Write to pandas dataframe
    df.to_csv(path_or_buf="result.csv", index=False)  # Write to csv
    '''

# Some sources:
# https://www.toptal.com/python/twitter-data-mining-using-python
# https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
# https://developer.twitter.com/en/docs/twitter-api/v1/geo/places-near-location/api-reference/get-geo-search
# https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location
# https://www.kdnuggets.com/2016/06/mining-twitter-data-python-part-1.html
# https://towardsdatascience.com/mining-twitter-data-ba4e44e6aecc
# https://www.linkedin.com/pulse/tweepy-tutorial-how-scrape-data-from-twitter-using-python-revanth
# https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1
# http://adilmoujahid.com/posts/2014/07/twitter-analytics/


