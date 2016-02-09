# TwitterStream

### Data Steam
This application utilizes Twitter Streaming API. More specifically, public streams from the API are fetched. The streams of data include tweets from all around the world in realtime. In addtion to the content, more information of the tweets are given in the JSON format of data, which is described in detail below.
The original information of the API can be found [here] (https://dev.twitter.com/streaming/public). Detailed application is develped with Python and [tweepy] (https://github.com/tweepy/tweepy) library.

##### Data Format
{"created_at":,
"id":,
"id_str":,
"text":,
"source":,
"truncated":,
"in_reply_to_status_id":,
"in_reply_to_status_id_str":,
"in_reply_to_user_id":,
"in_reply_to_user_id_str":,
"in_reply_to_screen_name":,
"user":,
"geo":,
"coordinates":,
"place":,
"contributors":,
"is_quote_status":,
"retwteet_count":,
"favorite_count":,
"entities":,
"favorited":,
"retweeted":,
"filter_level":,
"lang":,
"timestamp_ms":}
