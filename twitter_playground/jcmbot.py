import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# print(api.me())
user = api.me()

# print(user.followers_count)  # name, screen_name


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# FollowBackBot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     # if follower.name:
#     follower.follow()

# LikerBot - likes any tweet with given keyword
tbsearch = 'python'
numberOfTweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, tbsearch).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet! :)')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
