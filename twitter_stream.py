from retrying import retry
import os
import json
import unicodedata
import twitter

class TwitterStream:

    def __init__(self, track, filterList):
        self.track = track
        self.filterList = filterList
        self.api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                          consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                          access_token_key=os.environ['TWITTER_TOKEN_KEY'],
                          access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])


    @retry(wait_fixed=2000, stop_max_attempt_number=30)
    def run(self, writer, memorized=100):
        latestItems=[]
        for line in self.api.GetStreamFilter(track=self.track, languages=['en']):
            item = json.loads(json.dumps(line))
            try:
                text = unicodedata.normalize('NFKD', item['text']).encode('ascii','ignore')
                if(len(text)<20):
                    print('Too Short tweet:' + text)
                    continue
                duplicateFound=False
                for lItem in latestItems:
                    if(lItem==text):
                        duplicateFound=True
                        break
                if(duplicateFound):
                    # print 'Found duplicate : ' + text
                    continue
                #print 'No duplicates '+str(len(latestItems))
                if len(latestItems)<memorized:
                    latestItems.append(text)
                else:
                    latestItems.pop()
                    latestItems.append(text)

                # apply filters
                lowered=text.lower()
                if any(writer in lowered for writer in self.filterList):
                    continue
                #getting rid of bots data
                if ('high' in lowered) and ('low' in lowered) and ('change' in lowered):
                    continue
                if ('high' in lowered) and ('low' in lowered) and ('change' in lowered):
                    continue
                if ('high' in lowered) and ('low' in lowered) and ('volume' in lowered):
                    continue
                writer(text)

            except:
                print "[ERROR] failed to extract text."
