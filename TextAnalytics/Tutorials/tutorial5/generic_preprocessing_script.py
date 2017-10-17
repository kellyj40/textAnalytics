
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def pre_process_array(array_of_sentences):

    # 1st remove the stop words
    stops_removed_words = remove_stop_words_and_to_lower(array_of_sentences)
    stemmed_words = porter_stemming_words(stops_removed_words)

    return stemmed_words
    # 2nd stem words

# stop words to be removed
stop_words = stopwords.words('english')


def remove_stop_words_and_to_lower(array_of_sentences):

    stop_words = stopwords.words('english')
    removed_tokens = []

    for sentence in array_of_sentences:
        split_sentences = sentence.split()
        removed_tokens.append([word.lower() for word in split_sentences if word not in stop_words])

    return removed_tokens


def porter_stemming_words(array_of_words):
    ps = PorterStemmer()
    documents = [ps(word) for word in array_of_words]
    return documents




