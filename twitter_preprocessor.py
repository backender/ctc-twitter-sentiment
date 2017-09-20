import re
from model import *
import thread
import time
import datetime

db.get_conn()
db.create_table(TweetMidEth, safe=True)
db.create_table(TweetMidBtc, safe=True)

def PreprocessorEth(text,timeStamp,retry = 10):
    text=PreprocessText(text)
    #add to the database
    try:
        t = TweetMidEth(timestamp=timeStamp, text=text).save()
        #print str(timeStamp) + ": " + str(t) + " ETH tweet written to mid."
    except:
        if retry > 0:
            print "[ERROR] retry writing tweet: " + text
            time.sleep(2)
            thread.start_new_thread( PreprocessorEth, (text,timeStamp, retry-1) )
        else:
            print "[ERROR] failed writing tweet: " + text

    
def PreprocessorBtc(text,timeStamp,retry = 10):
    text=PreprocessText(text)
    #add to the database
    try:
        t = TweetMidBtc(timestamp=timeStamp, text=text).save()
        #print str(timeStamp) + ": " + str(t) + " ETH tweet written to mid."
    except:
        if retry > 0:
            print "[ERROR] retry writing tweet: " + text
            #writeTweetSentiment(text, scores, retry = retry-1)
            time.sleep(2)
            thread.start_new_thread( PreprocessorEth, (text,timeStamp, retry-1) )
        else:
            print "[ERROR] failed writing tweet: " + text
                       
def PreprocessText(text):
    #Remove non-alphabetic characters except toLeave
    #toLeave = " &#@!"
    #text = ' '.join(re.sub("^[a-zA-Z ]*$|[0-9 ]+|(\w+:\/\/\S+)"," ",text).split())
    #text = re.sub(r'[^\w'+toLeave+']', '',text)
    
    #Removing links
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
   
    # remove retweet prefix
    #if text.strip().startswith('RT '):
    #    text = text[2:]
    
    # lowercase
    text = text.lower()
    return text.rstrip()