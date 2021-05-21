import MeCab
import re

text = open("../text/keisuke_honda.txt","r").read()
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
text = text.translate(table).split()
url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

text = list(set(text)) # Remove duplicates

for i in range(10):
    for phrase in text:
    # for word in phrase:
        if re.match(url_pattern, phrase): # URL
            text.remove(phrase)
        elif bool(re.search(r'[a-zA-Z0-9]', phrase)):
            text.remove(phrase)
        elif re.match('^@.*', phrase):
            text.remove(phrase)
        elif re.match('.*,$', phrase):
            text.remove(phrase)
        elif re.match('^#.*', phrase):
            text.remove(phrase)
        elif re.match('RT', phrase):
            text.remove(phrase)

# Parse text using MeCab
m = MeCab.Tagger('-Owakati')
f = open('../text/new_keisuke_honda.txt', 'w')
for phrase in text:
    splited_phrase = m.parse(phrase)
    f.write(str(splited_phrase))
f.close()