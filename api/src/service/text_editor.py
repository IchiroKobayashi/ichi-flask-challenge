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

print(text)
for i in range(10):# TODO: 調査=>なんだか10回くらいやらないとちゃんと文字列が精製されない。
    for line in text:
    # for word in line:
        if re.match(url_pattern, line): # URL
            text.remove(line)
        elif bool(re.search(r'[a-zA-Z0-9]', line)):
            text.remove(line)
        elif re.match('^@.*', line):
            text.remove(line)
        elif re.match('.*,$', line):
            text.remove(line)
        elif re.match('^#.*', line):
            text.remove(line)
        elif re.match('RT', line):
            text.remove(line)

# Parse text using MeCab
m = MeCab.Tagger('-Owakati')
f = open('../text/new_keisuke_honda.txt', 'w')
for line in text:
    splited_line = m.parse(line)
    f.write(str(splited_line))
f.close()