
import pickle
import nltk
import math
import operator
import pprint

# Open up the objects from the scrapping
with open('word_count_dict.pickle', 'rb') as word_dict:
    dict_word_count = pickle.load(word_dict)

with open('total_num_of_words.pickle', 'rb') as total_words:
    total_word_count = pickle.load(total_words)

with open('tweets_stop_removal.txt', encoding='utf-8') as doc_file:
    documents = doc_file.read()
# Tokenize the documents
words = nltk.word_tokenize(documents)
# make bigrams of the words
bi_collection = nltk.bigrams(words)

# PMI calculations
def pmi_calculation(times_together, total_number_of_words, times_word1, times_word2):

    return math.log((times_together/total_number_of_words)/((times_word1/total_number_of_words)*(times_word2/
                                                                                                 total_number_of_words)))
bi_collection = list(bi_collection)


def pmi_dict(num_words, dict_word_count):
    # Two dictionaries
    dict_of_bi_no_limit = {}
    dict_of_bi_limit = {}
    for words in bi_collection:

        if bi_collection.count((words[0], words[1])) >= 2:
            pmi_val = pmi_calculation(bi_collection.count((words[0], words[1])), num_words, dict_word_count[words[0]], dict_word_count[words[1]])
            string_words = words[0] + " " +words[1]
            if string_words not in dict_of_bi_limit:
                dict_of_bi_limit[string_words] = pmi_val
        pmi_val_no_lim = pmi_calculation(bi_collection.count((words[0], words[1])), num_words, dict_word_count[str(words[0])], dict_word_count[str(words[1])])
        string_words = words[0] + " " + words[1]
        if string_words not in dict_of_bi_no_limit:
            dict_of_bi_no_limit[string_words] = pmi_val_no_lim

    return dict_of_bi_no_limit, dict_of_bi_limit


dict_of_bi_no_limit, dict_of_bi_limit = pmi_dict(total_word_count, dict_word_count)

# pretty print of the results
def print_sorted_dict(dict_rep):
    sorted_x = sorted(dict_rep.items(), key=operator.itemgetter(1))
    pprint.pprint(sorted_x)

print_sorted_dict(dict_of_bi_no_limit)
print_sorted_dict(dict_of_bi_limit)
