from nltk import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import nltk 
import os

# nltk.download('punkt')

with open('./data/text.txt', 'r', encoding="utf-8") as f:
  text = f.read()
  print(text)
  

# 2 - Tokenize the text  
sent_tokens = sent_tokenize(text)
word_tokens = word_tokenize(text)
print(len(sent_tokens))
print(len(word_tokens))

# 3 - Frequency of the Distribution
fdist = FreqDist(word_tokens)
print(fdist.most_common(10))
fdist.plot(10)