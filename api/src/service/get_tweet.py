import datetime, sys
import tweepy
sys.path.append('../')
import settings

# Auth: Set Keys & Secrets for Twitter API
auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# Generate Api Instance
api = tweepy.API(auth, wait_on_rate_limit = False)

# Set Account ID 
# q = 'keyword'
account = 'ichi_zamurai' # Include '@' whichever you like

# Get Tweets by Cursor & Put them into List
# tweets = api.user_timeline(account, count=3, tweet_mode='extended')
tweets = tweepy.Cursor(api.user_timeline, account, tweet_mode='extended').items(1)
# tweets = tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items()


tweet_texts = []
for tweet in tweets:
    # Convert UTC to JST
    jst_time = tweet.created_at + datetime.timedelta(hours=9)

    # Get Full Texts of Usertimeline Tweets
    # print('tweet: %s, jst_time: %s' % (tweet.full_text, jst_time))
    print(tweet)
    tweet_texts.append(tweet.full_text + '\n')

# Output as File
with open('../text/'+ account +'.txt', "w", encoding="utf-8") as f:
    f.writelines(tweet_texts)