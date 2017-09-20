
import nltk

def openFile(file_path_name):

    with open(file_path_name) as file:
        text = file.read()

    return text

paragraph = openFile("nltk_file2.txt")


token_words = nltk.word_tokenize(paragraph)

# porter stemming the words
stemmer = nltk.PorterStemmer()
stem_words = [stemmer.stem(wd) for wd in token_words]
print(token_words)
print(stem_words)

'''
Stemming the words has caused more mistakes
# This --> Thi
# divided --> divide and visited --> visit and travelled --> travel
# up-to-date --> up-to-d, motivated --> motiv
# O'Kelly --> O'Kelli , necessarily --> necessarili
# computing --> comput
# titles --> titl
# language --> languag
# systematically --> systemat
'''

# Leminization
pos_words = nltk.pos_tag(token_words)
lem_words = nltk.ne_chunk(pos_words, binary=True)
print(lem_words)







