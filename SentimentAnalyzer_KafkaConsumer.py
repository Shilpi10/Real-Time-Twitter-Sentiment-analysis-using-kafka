from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
from textblob import TextBlob
es = Elasticsearch()


def main():
    '''
    main function initiates a kafka consumer, initialize the tweetdata database.
    Consumer consumes tweets from producer extracts features, cleanses the tweet text,
    calculates sentiments and loads the data into postgres database
    '''
    # set-up a Kafka consumer
    #consumer = KafkaConsumer("twitter")
    for msg in KafkaConsumer("twitter"):
        #print(json.loads(msg.value))


        dict_data = json.loads(json.loads(msg.value))
        #print(dict_data["text"])

        tweet = TextBlob(dict_data["text"])
        print(tweet)
        if tweet.sentiment.polarity > 0:
            sentiment = "positive"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "negative"
        print(sentiment)
        # add text and sentiment info to elasticsearch
        es.index(index="sentiment",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "sentiment": sentiment
                       }
                 )
        print('\n')


if __name__ == "__main__":
    main()
