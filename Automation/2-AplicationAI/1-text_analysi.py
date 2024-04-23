from nltk import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
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

# 4 - World Cloud
def plot_cloud(word_cloud):
  plt.figure(figsize=(40, 30))
  plt.imshow(word_cloud, interpolation='bilinear')
  plt.axis('off')
  plt.show()
  
word_cloud = WordCloud(
  width = 3000,
  height = 2000,
  random_state = 1,
  background_color = 'salmon',
  colormap = 'Pastel1',
  collocations = False,
  stopwords = STOPWORDS
).generate(text)

# plot_cloud(wordcloud)

mascara = np.array(
    Image.open("data/upvote.png")
)

word_cloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color= 'salmon',
    colormap = 'Pastel1',
    collocations = False,
    stopwords = STOPWORDS,
    mask = mascara
).generate(text)

plot_cloud(word_cloud)