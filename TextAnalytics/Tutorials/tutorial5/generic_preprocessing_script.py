
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

def pre_process_array(array_of_documents):

    # 1st remove special characters
    remove_special_characters_arr = remove_special_characters(array_of_documents)

    # 2nd remove the stop words
    stops_removed_words = remove_stop_words_and_to_lower(remove_special_characters_arr)

    # 3rd Stem words
    # stemmed_words = porter_stemming_words(stops_removed_words)

    # 4th frequency of words TF values
    freq_of_words_per_doc, freq_of_words_all = calculate_frequency_words(stops_removed_words)

    return "not stemmed", freq_of_words_per_doc, freq_of_words_all

# stop words to be removed
stop_words = stopwords.words('english')

def remove_special_characters(array_documents):

    remove_special_arr = [re.sub('[^A-Za-z0-9]+'," ", document) for document in array_documents]
    return remove_special_arr

def remove_stop_words_and_to_lower(array_of_sentences):

    stop_words = stopwords.words('english')
    removed_tokens = []

    for sentence in array_of_sentences:
        split_sentences = sentence.split()
        removed_tokens.append([word.lower() for word in split_sentences if word not in stop_words])

    return removed_tokens


def porter_stemming_words(array_of_documents):
    ps = PorterStemmer()
    stemmed_words = []
    for document in array_of_documents:
        stemmed_words.append([ps.stem(word) for word in document])
    return stemmed_words


def calculate_frequency_words(documents):
    # Make dict to contain words
    documents_of_countes = []
    dict_of_all_words = {}
    # Seperate out the documents
    for document in documents:
        dict_of_all_words_per_doc = {}
        # Add each word to the dictionary in the document
        for word in document:
            # if its not already int the dictionary then add it
            if word not in dict_of_all_words:
                dict_of_all_words[word] = 1
                dict_of_all_words_per_doc[word] = 1
            elif word not in dict_of_all_words_per_doc:
                dict_of_all_words[word] += 1
                dict_of_all_words_per_doc[word] = 1
            else:
            # Other wise add one to the current value
                dict_of_all_words[word] += 1
                dict_of_all_words_per_doc[word] += 1

        documents_of_countes.append(dict_of_all_words_per_doc)

    return documents_of_countes, dict_of_all_words




