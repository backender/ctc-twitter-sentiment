from twitter_stream import *
import tweet_writer as writer

track = ['btc', 'bitcoin', 'xbt', 'satoshi']

hashtags = ['#mpgvip', '#freebitcoin', '#makeyourownlane', '#footballcoin']
words = ['entertaining', 'subscribe', 'free']
bigrams = ['current price', 'bitcoin price', 'earn bitcoin']
trigram = ['start trading bitcoin']
filterList = hashtags + words + bigrams + trigram

stream = TwitterStream(track, filterList)
stream.run(writer.writeTweetSentiment)
