# Imports
from bs4 import BeautifulSoup as bs
import requests
import nltk
import pickle

from nltk.tokenize import RegexpTokenizer

# URL link to bloomberg
url = "https://www.bloomberg.com/europe"

# Make the request
html_object = requests.get(url)
data_html = html_object.text

# Make Beautiful soup object and pass in html code
soup = bs(data_html, "html5lib")

# Special characters remover and end of words
tokenizer = RegexpTokenizer(r'\w+')

# Remove tokenisation and special characters
array_of_words = []
for element in soup.select('h1'):
    line = element.get_text().replace(".", "")
    array_of_words.append(tokenizer.tokenize(line))

# Reomove stop words, I, me, my etc..
stopset = set(nltk.corpus.stopwords.words('english'))

# Add two words to the stop words
stopset.add("menu")
stopset.add("trending")
# Remove the stop words, compare to lower case or doesnt work, make it a list
removed_stops = [word for word_array in array_of_words for word in word_array if word.lower() not in stopset]


# dictionary to keep counter of the words
dict_of_words = {}
for word in removed_stops:
    if word not in dict_of_words:
        dict_of_words[word] = 1
    else:
        dict_of_words[word] += 1

# Open old dictionary of words
with open('bloomberg_news.pkl', 'rb') as f:
    old_dict_of_words = pickle.load(f)
    f.close()

# Add Most recent count to the word count
for key in dict_of_words:
    if key in old_dict_of_words:
        old_dict_of_words[key] += dict_of_words[key]
    else:
        old_dict_of_words[key] = dict_of_words[key]

with open('bloomberg_news.pkl', 'wb') as f:
    pickle.dump(old_dict_of_words, f)          # dump data to f
    f.close()

