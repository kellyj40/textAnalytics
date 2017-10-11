import nltk
stemmer = nltk.PorterStemmer()
print(stemmer.stem("children"))
print(stemmer.stem("childrens"))
print(stemmer.stem("children's"))
