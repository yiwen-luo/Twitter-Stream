#!/usr/bin/python
from sys import stdout
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json


def main():
    # Authentication information for Twitter API
    consumer_key = "" #YOUR OWN KEY HERE
    consumer_secret = "" #YOUR OWN KEY HERE
    access_token = "" #YOUR OWN KEY HERE
    access_key = "" #YOUR OWN KEY HERE

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_key)

    twitter_stream = Stream(auth, Listener())
    twitter_stream.filter(locations=[-180,-90,180,90], async=False)


class Listener(StreamListener):

    def on_data(self, data):
        received_data = json.loads(data)
        try:
            print json.dumps({'lat': received_data['geo']['coordinates'][0],
                              'lng': received_data['geo']['coordinates'][1]})
            stdout.flush()
        except:
            pass
        return True

    def on_error(self, status):
        print status


if __name__ == "__main__":
    main()
