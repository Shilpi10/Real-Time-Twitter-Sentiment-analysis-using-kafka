from kafka import KafkaProducer
import kafka
import json
import tweepy
import re
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# TWITTER API CONFIGURATIONS
consumer_key = "HQRSo04ugoubMB38yh15D7zcc"
consumer_secret = "PxCaE71YqQVD8mE1DYPhmE3ZcggXA6Z1jBeoexiFHZ5jtsTFgv"
access_token = "831114864244436992-2TH4npvjcQaDKXTkJSqdYhzm6WitjG2"
access_secret = "f3ICcmfVGMg3oFZqZnmU1zkkGqQz6QHmBpejz9mgWAHmp"

# TWITTER API AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer = lambda m :json.dumps(m).encode('ascii'))

    # Get Producer that has topic name is Twitter

    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("twitter", data)
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True


# Twitter Stream Config
twitter_stream = Stream(auth, KafkaPushListener())

# Produce Data that has trump and coronavirus hashtag (Tweets)
twitter_stream.filter(track=['#trump','#coronavirus'])

