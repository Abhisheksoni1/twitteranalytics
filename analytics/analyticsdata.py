from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
# Variables that contains the user credentials to access Twitter API
access_token = "2407157197-uDJCl4TIjVIFj9RTmBIdmbUHtAiXoPqDek5PXQl"
access_token_secret = "2pJ2W2ayolwIyRcXUbK101uoYvI6w9WtZwrlQ5rV81t8T"
consumer_key = "DfQNOEplBwPASLFSjST2XnPkM"
consumer_secret = "XHp8EZtKLKGeQeYy2PyhKnzTxP6ItCQLJWwn9JZu20XMtMIf1L"

# Data structure for our Data model
DATA_DICT = {'created': '', 'post_id': '', 'text': '', 'location': ''}


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        DATA_DICT['created'] = data['created_at']
        DATA_DICT['post_id'] = data['id']
        DATA_DICT['text'] = data['text']
        DATA_DICT['location'] = data['place']['country'] if data['place'] != None else "Others"
        print DATA_DICT
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keyword: analytics
    stream.filter(track=['analytics'])
