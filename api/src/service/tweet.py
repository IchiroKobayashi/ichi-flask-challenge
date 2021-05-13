# -*- coding: utf-8 -*-
import markovify

with open('../text/learned_data.json', 'r') as f:
    text_model = markovify.Text.from_json(f.read())

for i in range(3):
    print(text_model.make_short_sentence(140))