import thread
import time
import datetime
from model import *
from twitter_preprocessor import *

db.get_conn()
db.create_table(TweetEarlyEth, safe=True)
db.create_table(TweetEarlyBtc, safe=True)

def writeTweetsEarlyDelayed(text, retry = 10):
    time.sleep(3)
    writeTweetsEarly(text, retry)

def writeTweetsEarly(text, retry = 10):
    timeStamp = datetime.datetime.utcnow()
    try:
        textLowered=text.lower()
        if(('ethereum' in textLowered) or ('eth' in textLowered)):
            t = TweetEarlyEth(timestamp=timeStamp, text=text).save()
            #print str(timeStamp) + ": " + str(t) + " ETH tweet written to early."
            thread.start_new_thread( PreprocessorEth, (text,timeStamp) )
        if(('bitcoin' in textLowered) or ('btc' in textLowered) or ('xbt' in textLowered)):
            t = TweetEarlyBtc(timestamp=timeStamp, text=text).save()          
            #print str(timeStamp) + ": " + str(t) + " BTC tweet written to early."
            thread.start_new_thread( PreprocessorBtc, (text,timeStamp) )
    except:
        if retry > 0:
            print "[ERROR] retry writing tweet: " + text
            #writeTweetSentiment(text, scores, retry = retry-1)
            thread.start_new_thread( writeTweetsEarlyDelayed, (text, retry-1) )
        else:
            print "[ERROR] failed writing tweet: " + text
