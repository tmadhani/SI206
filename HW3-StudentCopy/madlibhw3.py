# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk
from nltk.book import text2
from nltk import word_tokenize,sent_tokenize

def text_from_file(filename):
    raw = open(filename)
    text = raw.read()
    raw.close()
    return text
print(text_from_file(text2))
# f = open(text2, 'r')
# para = f.read()
# tokens = texts(text2)
# print(tokens)
# print("TOKENS")
# print(tokens)
# tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:5]:
# 		print (tup)

print("\n\nEND*******")
