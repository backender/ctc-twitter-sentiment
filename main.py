import json
import os
import re
import twitter
import unicodedata
from vaderSentiment import vaderSentiment

analyzer = vaderSentiment.SentimentIntensityAnalyzer()

api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWITTER_TOKEN_KEY'],
                  access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])

track = ['btc', 'bitcoin', 'xbt', 'satoshi']

hashtags = ['#mpgvip', '#freebitcoin', '#makeyourownlane', '#footballcoin']
words = ['entertaining', 'subscribe', 'free']
bigrams = ['current price', 'bitcoin price', 'earn bitcoin']
trigram = ['start trading bitcoin']
filterList = hashtags + words + bigrams + trigram

for line in api.GetStreamFilter(track=track, languages=['en']):
        response = json.loads(json.dumps(line))
        text = response['text']

        # remove everything non-alphabetic but removelist
        removelist = " &#@"
        text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
        text = ' '.join(re.sub("^[a-zA-Z ]*$|[0-9 ]+|(\w+:\/\/\S+)"," ",text).split())
        text = re.sub(r'[^\w'+removelist+']', '',text)

        # remove retweet prefix
        if text.strip().startswith('RT '):
            text = text[2:]

        # lowercase & apply filters
        text = text.lower()
        if any(f in text for f in filterList):
            continue

        print text
        print analyzer.polarity_scores(text)
        #print response
