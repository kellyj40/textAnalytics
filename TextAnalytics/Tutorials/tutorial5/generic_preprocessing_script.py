
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def pre_process_array(array_of_sentences):

    # 1st remove the stop words
    stops_removed_words = remove_stop_words_and_to_lower(array_of_sentences)

    # 2nd Stem words
    stemmed_words = porter_stemming_words(stops_removed_words)

    # 3rd frequency of words
    freq_of_words = calculate_frequency_words(stemmed_words)

    return stemmed_words, freq_of_words

# stop words to be removed
stop_words = stopwords.words('english')


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
        stemmed_words.append([ps(word) for word in document])
    return stemmed_words


def calculate_frequency_words(documents):
    # Make dict to contain words
    dict_of_all_words = {}
    # Seperate out the documents
    for document in documents:
        # Add each word to the dictionary in the document
        for word in document:
            # if its not already int the dictionary then add it
            if word not in dict_of_all_words:
                dict_of_all_words[word] = 1
            else:
            # Other wise add one to the current value
                dict_of_all_words[word] += 1

    return dict_of_all_words



