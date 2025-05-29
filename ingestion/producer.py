import tweepy
from kafka import KafkaProducer
import json
import os
from dotenv import load_dotenv

load_dotenv()

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

class StreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"Tweet: {tweet.text}")
        producer.send('twitter_stream', tweet.data)

stream = StreamListener(bearer_token=os.getenv("TWITTER_BEARER_TOKEN"))
stream.add_rules(tweepy.StreamRule("data engineering"))
stream.filter(tweet_fields=["created_at", "lang"])
