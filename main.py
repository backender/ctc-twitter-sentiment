import tweet_writer as writer
from twitter_streamer import *

tracker = ['ethereum','eth','btc', 'bitcoin', 'xbt']

word = ['entertaining', 'subscribe', 'free','android','tokensale']
hashtag = ['#mpgvip', '#freebitcoin', '#makeyourownlane', '#footballcoin','@sexservice']
bigram = ['current price', 'bitcoin price', 'earn bitcoin','free trading','android app','join moneypot','join our']
trigram = ['start trading bitcoin','satoshis best kept','join daily signals','hash rush update','in real estate','invest in our','we are accepting','join the ico']
toFilter= word+ hashtag + bigram + trigram

streamer = TwitterStreamer(tracker, toFilter)
streamer.run(writer.writeTweetsEarly)
