import pandas as pd
import tweepy

class ApiData:

    def get_twitter_data_by_hashtag(self, hashtag, num_tweets):
        api = self._init_twitter_auth()
        tweets = tweepy.Cursor(api.search, q=hashtag, count=10).items(num_tweets)

        # https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
        tweet_text = [[tweet.id, tweet.user.screen_name, tweet.user.location,
                       tweet.user.followers_count, tweet.user.friends_count,
                       tweet.user.listed_count, tweet.user.favourites_count,
                       tweet.user.statuses_count,
                       tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                       tweet.retweet_count, tweet.favorite_count,
                       tweet.text] for tweet in tweets]
        #print(tweet_text[:1])

        tweet_df = pd.DataFrame(data=tweet_text,
                                columns=['user_id', 'user', 'location',
                                         'user_follower_count', 'user_friends_count',
                                         'user_listed_count', 'user_favorites_count',
                                         'user_statuses_count',
                                         'tweet_created_time',
                                         'retweet_count', 'favorite_count',
                                         'text'])
        #print(tweet_df.columns)
        #print(tweet_df.get_values())
        return tweet_df

    def _init_twitter_auth(self):
        ACCESS_TOKEN = '<enter your own>'
        ACCESS_SECRET = '<enter your own>'
        CONSUMER_KEY = '<enter your own>'
        CONSUMER_SECRET = '<enter your own>'

        # Setup tweepy to authenticate with Twitter credentials:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Create the api to connect to twitter with your creadentials
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

        return api


if __name__ == '__main__':
    o = ApiData()
    df = o.get_api_data()
    print(df.columns)
    print(df.count())
    print(df.to_string())

    tweets = o.get_twitter_data_by_hashtag('#captainmarvel', 100)
    print(tweets.count())
    print(tweets.columns)


