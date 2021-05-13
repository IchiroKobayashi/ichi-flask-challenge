from flask import jsonify
import settings
import re
import MeCab
import markovify


API_KEY = settings.AP

# TODO: 引数受け取る
def scrape_logic():
    edit_text()
    make_dictionary()
    tweets = tweet()
    result = {
        "tweets": tweets,
    }
    # TODO: model使ってmysqlにツイートを保存する。
    return jsonify(result)

def edit_text():
    # TODO: tweetAPI 取得
    with open("./text/keisuke_honda.txt","r") as f:
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
    f = open('./text/new_keisuke_honda.txt', 'w')
    for line in texts:
        splited_line = m.parse(line)
        f.write(str(splited_line))
    f.close()


def make_dictionary():
    # Load file
    with open("./text/new_keisuke_honda.txt", "r") as f:
        text = f.read()

    # Build model
    text_model = markovify.NewlineText(text, state_size=3, well_formed=False) # e.g. state_size=2: John ate, state_size=5: John ate a bagel with

    # Make Dictionary as Json_format
    with open('./text/learned_data.json', 'w') as f:
        f.write(text_model.to_json())


def tweet():
    with open('./text/learned_data.json', 'r') as f:
        text_model = markovify.Text.from_json(f.read())

    tweets = []
    for _ in range(10):
        tweet = text_model.make_short_sentence(140)
        tweet = tweet.replace(' ', '')
        print(tweet)
        tweets.append(tweet)
    # TODO: tweetAPI
    return tweets