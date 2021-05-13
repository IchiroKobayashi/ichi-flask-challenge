import markovify

# Load file
text = open("../text/new_keisuke_honda.txt", "r").read()

# Build model
text_model = markovify.NewlineText(text, state_size=3, well_formed=False)

# Make Dictionary as Json_format
with open('../text/learned_data.json', 'w') as f:
    f.write(text_model.to_json())