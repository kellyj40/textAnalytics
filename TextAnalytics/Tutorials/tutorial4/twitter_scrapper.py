'''Twitter scrape - can be used by the
tweepy package, twitter package or oauth2
tweepy seems most popular and easiest for streamming tweets
but couldnt find example for getting topic so used the twitter one
'''
#-------------- Keys --------------------#
consumer_key = "U56cEVZ9IAJYfInVZCLs4vggB"
consumer_secret = "cqz2KqIeZekLm9EGHsZY1UtVk7S8uUi69nD8ORgHcEQcsx9bLU"
access_token = "490216973-e3fWUMA6S2LTaCExJYlH1Lhlpxamk4Cal2fndEP7"
access_secret = "BhviGuJpg0phbH70VU5WPxQaLxc1c4e20g8CC9tNfSLIy"

'''Getting topic and saving to the json file'''
#-------------- import --------------------#
from twitter import Twitter, OAuth
import json

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)
# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

def stream_topic_from_twitter(topic):

    # Search for latest tweets about "#hurricane"
    result = twitter.search.tweets(q='#'+topic, result_type='recent', lang='en', count=50)

    data_dict = dict(result)

    json_data_to_file = json.dumps(data_dict)
    # first method of opening file and writing too
    file = open("json_tweets.json", "w")
    file.write(json_data_to_file)

def open_saved_twitter_file():
    # another method of writing to file
    with open('json_tweets.json') as data_file:
        data = json.load(data_file)

    return data

# stream_topic_from_twitter("hurricane")
json_data = open_saved_twitter_file()

def split_tweets_from_data(json_data):
    number_of_tweets = json_data['search_metadata']['count']
    tweet_section = json_data['statuses']
    list_of_tweets = []


    # loop through the tweets - collecting and storing in the list
    for tweet in tweet_section:
        list_of_tweets.append(tweet["text"])

    return list_of_tweets

list_of_tweets = split_tweets_from_data(json_data)


from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
stop_words = stopwords.words('english')
stop_words.append("RT")
def nltk_remove_stops(list_of_tweets):
    tweets_stop_word_removal = []
    tokenizer = RegexpTokenizer(r'\w+')
    for sentence in list_of_tweets:

        sentence = sentence.split()  # split on spaces to make into list
        # lots in this line, first get all words in each sentence that is not a stopWord, begins with @ or https
        # With them words, convert to lower and tokenize to remove # and other punctuations
        # tokenizer returns list, want a string of just the word, so make into string by joining to empty string
        filtered_words = [''.join(tokenizer.tokenize(word.lower())) for word in sentence if word not in stop_words and not word.startswith("@") and not word.startswith("https") and not word.startswith("http") and not word.startswith("htt")]
        tweets_stop_word_removal.append(filtered_words)
    return tweets_stop_word_removal

removed_stop_words_tweets = nltk_remove_stops(list_of_tweets)

def saving_list_to_txt(removed_stop_words_tweets):
    count = 0
    tracker = []
    remove_index = []
    removed_duplicates = []
    with open("tweets_stop_removal.txt", "w") as file:

        while count < len(removed_stop_words_tweets):
            sentence = ""
            for word in removed_stop_words_tweets[count]:
                sentence+=word+" "
            sentence += "\n"
            if sentence in tracker:
                remove_index.append(count)
                pass
            else:
                tracker.append(sentence)
                file.write(sentence)

            count += 1
    count = 0
    while count<len(removed_stop_words_tweets):
        if count in remove_index:
            pass
        else:
            removed_duplicates.append(removed_stop_words_tweets[count])
        count += 1

    return removed_duplicates



removed_stop_words_tweets = saving_list_to_txt(removed_stop_words_tweets)
print(removed_stop_words_tweets)

def text_frequency_count(removed_stop_words_tweets):
    # Convert into 1d array
    words_after = [j for i in removed_stop_words_tweets for j in i]
    dictionary_words = {}
    list_of_words = []
    for word in words_after:
        if word not in dictionary_words:
            dictionary_words[word] = 1
            list_of_words.append(word)
        else:
            dictionary_words[word] += 1
    return dictionary_words, list_of_words

freq_term_dict, list_of_words = text_frequency_count(removed_stop_words_tweets)

import operator
import pprint
def print_sorted_dict(dict_rep):
    sorted_x = sorted(dict_rep.items(), key=operator.itemgetter(1))
    pprint.pprint(sorted_x)

print_sorted_dict(freq_term_dict)

def n_containing_word(set_of_documents, list_of_words):
    dict_of_number_of_documents = {}
    for word in list_of_words:
        for document in set_of_documents:
            if word in document:
                if word in dict_of_number_of_documents:
                    dict_of_number_of_documents[word] += 1
                else:
                    dict_of_number_of_documents[word] = 1
    return dict_of_number_of_documents
dict_of_number_of_documents = n_containing_word(removed_stop_words_tweets, freq_term_dict)
# print_sorted_dict(dict_of_number_of_documents)


import math
def tf_idf_scores(number_of_appearence, number_of_documents, set_of_documents):
    '''loop through each document, compare each word to the total of occurrance in all documents and make score'''
    tf_idf_dictionary = {}
    length_of_documents = len(set_of_documents)
    for key, value in number_of_appearence.items():
        if value >= 3:
            tf_idf_dictionary[key] = round(math.log(int(length_of_documents)/(int(number_of_documents[key])))*20)
    return tf_idf_dictionary
tf_idf_dictionary = tf_idf_scores(freq_term_dict, dict_of_number_of_documents, removed_stop_words_tweets)
print_sorted_dict(tf_idf_dictionary)


def text_file_of_idf_scores(tf_idf_dictionary):
    with open("idf_scores.txt", "w") as file:
        for key, value in tf_idf_dictionary.items():
            count = 0
            while count < value:
                file.write(key + " ")
                count+=1
            file.write("\n")

text_file_of_idf_scores(tf_idf_dictionary)

import pickle

def save_object_of_words(set_of_documnets, word_count_dict):
    with open("all_documents.pickle", "wb") as file_pickle:
        pickle.dump(set_of_documnets, file_pickle)

    with open("word_count_dict.pickle", "wb") as file_pickle:
        pickle.dump(word_count_dict, file_pickle)

    with open("total_num_of_words.pickle", "wb") as file_pickle:
        number_of_words = 0
        for key, value in freq_term_dict.items():
            number_of_words += value
        pickle.dump(number_of_words, file_pickle)

save_object_of_words(removed_stop_words_tweets, freq_term_dict)

'''Once the file is saved into a json file, in this case python.json
Then need to do processing on the tweets.'''

# import json
#
# with open('hurricane.json', 'r') as f:
#     line = f.readline()  # read only the first tweet/line
#     tweet = json.loads(line)  # load it as Python dict
#     print(json.dumps(tweet, indent=4))  # pretty-print




'''In case we want to “keep the connection open”, and gather all the upcoming tweets about a particular event,
the streaming API is what we need. We need to extend the StreamListener() to customise the way we process the incoming data.
A working example that gathers all the new tweets with the #python hashtag:'''

# from tweepy import Stream
# from tweepy.streaming import StreamListener
#
#
# class MyListener(StreamListener):
#     def on_data(self, data):
#         try:
#             with open('hurricane.json', 'a') as f:
#                 f.write(data)
#                 return True
#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#         return True
#
#     def on_error(self, status):
#         print(status)
#         return True
#
#
# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['#hurricane']) #This is the tag trying to get

'''
                Attributes of the json file include the following:
text: the text of the tweet itself
created_at: the date of creation
favorite_count, retweet_count: the number of favourites and retweets
favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
lang: acronym for the language (e.g. “en” for english)
id: the tweet identifier
place, coordinates, geo: geo-location information if available
user: the author’s full profile
entities: list of entities like URLs, @-mentions, hashtags and symbols
in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
in_reply_to_status_id: status identifier id the tweet is a reply to a specific status
'''







'''reading our own timeline'''
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status.text)

'''reading our followers'''
# for friend in tweepy.Cursor(api.friends).items():
#     process_or_store(friend._json)

'''reading our own tweets'''
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     process_or_store(tweet._json)

'''This method below uses tweepy, get tweets from a user'''
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)`  # This is authentication process.
# Get 20 tweets of a user ABCD on a topic
# new_tweets = api.user_timeline(screen_name ='ABCD',count=20)



'''This method below uses oauth'''
import oauth2 as oauth


# CONSUMER_KEY = "RikNDmtAvrPQY2fqNODuP92oq"
# CONSUMER_SECRET = "1ciXbFiLFKND03MpMDRx0hIEHXn3lgoTyzr0XenKjWItLrQavh"
#
# ACCESS_KEY = "490216973-9IfxzqlDIL3g5UY5ek0LQhIdyYLeF9suH9apTlf9"
# ACCESS_SECRET = "heKf66SKANBPSrPOboFPCe8XV3bvwk11SVahUt1TBzURC"
#
# consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
# access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
# client = oauth.Client(consumer, access_token)
#
# timeline_endpoint = "https://api.twitter.com/1.1/trends/place.json?id=1"
# response, data = client.request(timeline_endpoint)
# data = data.decode('utf-8')
#
# tweets = json.loads(data)
# print(tweets)


# for tweet in tweets:
#     print(tweet['text'])