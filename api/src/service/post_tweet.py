# -*- coding: utf-8 -*-
import markovify
import tweepy
import sys
sys.path.append('../')
import settings

if __name__ == '__main__':
    # Auth: Set Keys & Secrets for Twitter API
    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)
    auth.set_access_token(settings.HONDA_ACCESS_TOKEN, settings.HONDA_ACCESS_TOKEN_SECRET)

    # Generate Api Instance
    api = tweepy.API(auth)

    with open('../text/learned_keisuke_honda.json', 'r') as f:
        text_model = markovify.Text.from_json(f.read())
    tweet = text_model.make_short_sentence(140).replace(' ','')
    print(tweet)
    api.update_status(tweet)