import thread
import time
import datetime
from model import *

db.connect()
db.create_table(Tweet, safe=True)

def writeTweetSentimentDelayed(text, scores, retry = 10):
    time.sleep(3)
    writeTweetSentiment(text, scores, retry)

def writeTweetSentiment(text, scores, retry = 10):
    ts = datetime.datetime.utcnow()
    try:
        t = Tweet(timestamp=ts, text=text, positive=scores['pos'], negative=scores['neg'], neutral=scores['neu']).save()
        print str(ts) + ": " + str(t) + " tweet written."
    except:
        if retry > 0:
            print "[ERROR] retry writing tweet: " + text + "score: " + str(scores)
            #writeTweetSentiment(text, scores, retry = retry-1)
            thread.start_new_thread( writeTweetSentimentDelayed, (text, scores, retry-1) )
        else:
            print "[ERROR] failed writing tweet: " + text + "score: " + str(scores)
