from flask import jsonify
import os
import settings
import re
import MeCab
import markovify
import tweepy


def scrape_logic_by_id(account_id, limit):
    if not os.path.exists('../text/'+ account_id +'.txt'): # TODO: ハッシュ化して差分があったらTextファイル更新とか
        if account_id != 'keisuke_honda':
            get_tweets(account_id)
        edit_text(account_id)
        make_dictionary(account_id)
    morph_tweets = get_morph_tweets(account_id, limit)
    result = {
        "tweets": morph_tweets,
    }
    # TODO: model使ってmysqlにツイートを保存する。
    return jsonify(result)

def get_tweets(account_id):
    # Auth: Set Keys & Secrets for Twitter API
    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    # Generate Api Instance
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)

    # Set Account ID 
    # q = 'keyword'
    account = account_id # Include '@' whichever you like

    # Get Tweets by Cursor & Put them into List
    tweets = tweepy.Cursor(api.user_timeline, account, tweet_mode='extended').items(100)
    # tweets = api.user_timeline(account, count=3, tweet_mode='extended')
    # tweets = tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items()

    tweet_texts = []
    for tweet in tweets:
        tweet_texts.append(tweet.full_text + '\n')

    # Output as File
    with open('./text/'+ account +'.txt', "w", encoding="utf-8") as f:
        f.writelines(tweet_texts)
    return tweets


def edit_text(account_id):
    with open('./text/'+ account_id +'.txt','r') as f:
        text = f.read()
        table = str.maketrans({
                # '\n': '',
                # '\r': '',
                '(': '（',
                ')': '）',
                '[': '［',
                ']': '］',
                '"':'”',
                "'":"’",
            })
        texts = text.translate(table).split()
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

    for _ in range(10):# TODO: 10回くらいやらないとちゃんと文字列が精製されない。->指定した値と同じ要素を検索し、最初の要素を削除: remove()
        for line in texts:
        # for word in line:
            if re.match(url_pattern, line): # URL
                texts.remove(line)
            elif bool(re.search(r'[a-zA-Z0-9]', line)):
                texts.remove(line)
            elif re.match('^@.*', line):
                texts.remove(line)
            elif re.match('.*,$', line):
                texts.remove(line)
            elif re.match('^#.*', line):
                texts.remove(line)
            elif re.match('RT', line):
                texts.remove(line)

    # Parse text using MeCab
    m = MeCab.Tagger('-Owakati')
    f = open('./text/new_'+ account_id +'.txt', 'w')
    for line in texts:
        splited_line = m.parse(line)
        f.write(str(splited_line))
    f.close()


def make_dictionary(account_id):
    # Load file
    with open('./text/new_'+ account_id +'.txt', 'r') as f:
        text = f.read()

    # Build model
    text_model = markovify.NewlineText(text, state_size=2, well_formed=False) # e.g. state_size=2: John ate, state_size=5: John ate a bagel with

    # Make Dictionary as Json_format
    with open('./text/learned_'+ account_id +'.json', 'w') as f:
        f.write(text_model.to_json())


def get_morph_tweets(account_id, limit):
    with open('./text/learned_'+ account_id +'.json', 'r') as f:
        text_model = markovify.Text.from_json(f.read())

    tweets = []
    for _ in range(limit):
        tweet = text_model.make_short_sentence(140)
        tweet = tweet.replace(' ', '')
        print(tweet)
        tweets.append(tweet)
    # TODO: tweetAPI
    return tweets