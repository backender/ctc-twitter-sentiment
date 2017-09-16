import json
import re
import unicodedata
import twitter
from vaderSentiment import vaderSentiment
import os
from retrying import retry

class TwitterStream:

    def __init__(self, track, filterList):
        self.track = track
        self.filterList = filterList
        self.analyzer = vaderSentiment.SentimentIntensityAnalyzer()
        self.api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                          consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                          access_token_key=os.environ['TWITTER_TOKEN_KEY'],
                          access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])

    def extract_text(self, response):
        text = response['text']

        # remove everything non-alphabetic but removelist
        removelist = " &#@"
        text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
        text = ' '.join(re.sub("^[a-zA-Z ]*$|[0-9 ]+|(\w+:\/\/\S+)"," ",text).split())
        text = re.sub(r'[^\w'+removelist+']', '',text)

        # remove retweet prefix
        if text.strip().startswith('RT '):
            text = text[2:]

        # lowercase
        text = text.lower()

        return text

    @retry(wait_fixed=2000, stop_max_attempt_number=30)
    def run(self, f):
        for line in self.api.GetStreamFilter(track=self.track, languages=['en']):
            response = json.loads(json.dumps(line))
            try:
                text = self.extract_text(response)
                # apply filters
                if any(f in text for f in self.filterList):
                    continue

                f(text, self.analyzer.polarity_scores(text))
            except:
                print "[ERROR] failed to extract text."
