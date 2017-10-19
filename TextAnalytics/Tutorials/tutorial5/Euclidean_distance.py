import math
from generic_preprocessing_script import pre_process_array

# Documents / tweets
documents = ["Machine random words are in here learning will help computers learn algorithms and organized into taxonomy, based on the desired outcome of the algorithm. Common algorithm types include Supervised learning where the algorithm its self learns to generates a function that maps inputs to desired outputs. One standard formulation of the supervised learning task is the classification problem will learn: the learner is required to learn (to approximate the behavior of) a function which maps a vector into one of several classes by looking at several input-output examples of the function.",
             "Supervised some others are also now inserted in this one learning is the machine learning task of inferring a function from labeled training data. The training data consist of a set of training examples. In supervised learning, each example is a pair consisting of an input object (typically a vector) and learn a desired output value (also called the supervisory signal). A supervised learning algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples",
             "Unsupervised machine learning is the machine learning task of inferring a function to describe hidden structure from unlabeled data (a classification or categorization is not included in the observations). Since the examples given to the learner are unlabeled, there is no evaluation of the accuracy of the structure that is output by the relevant algorithm—which is one way of distinguishing unsupervised learning from supervised learning and reinforcement learning.",
             "Machine algorithms are based on the desired outcome of the algorithms. There are two types, Supervised learning and unsupervised learning techniques, where the algorithm generates a function that maps inputs to desired outputs. One standard formulation of the supervised task is the classification problem. Unsupervised learning which models a set of tasks: labeled examples are not available at the moment.",
             "Machine learning algorithms are organized into two categories, based on the desired outcome of the algorithm. Common algorithm types include Supervised learning and unsupervised learning techniques, where the algorithm generates a function that will map inputs to desired outputs or related results. One standard formulation of the supervised learning task is the classification problem of seperation. Unsupervised learning which models a set of inputs and outputs: labeled examples are not available.",
             "ML algorithms are organized into two seperate groups, based on the desired outcome of the algorithm. Common algorithm types include Supervised learning and unsupervised learning techniques, where the algorithm generates a function that maps inputs to desired outputs. One standard formulation of the supervised learning task is the classification problem. Unsupervised learning which models a set of inputs: labeled examples are not available.",
             "Machine learning algorithms are organized into two categories. These are Supervised learning and unsupervised learning techniques, where the algorithm generates a function for mapping. One standard formulation of the supervised learning task is the classification problem. Unsupervised learning which models a set of inputs: labeled examples are not available."]
# Use generic pre-processing script
cleaded_words, freq_of_words_per_doc, freq_of_words_all = pre_process_array(documents)


# computes TF-IDF
def compute_vector_len(doc_dict, df_count):
    tf_idf_dictionary = {}
    length_of_documents = len(doc_dict)
    for key, value in doc_dict.items():
        if value >= 0:
            tf_idf_dictionary[key] = round(math.log(int(length_of_documents) / (int(freq_of_words_all[key]))), 2)
    return tf_idf_dictionary


idf_scores = []
for doc_freq in freq_of_words_per_doc:

    idf_per_doc = compute_vector_len(doc_freq, freq_of_words_all)
    idf_scores.append(idf_per_doc)

print(idf_scores)
# Calculate the Ecliliadian distance
def get_Eucilian():
    counter = 0
    cosine_scores = []
    while counter < len(documents)-1:
        counter2 = counter+1
        while counter2 < len(documents):
            vec1 = idf_scores[counter]
            vec2 = idf_scores[counter2]

            all_words = set(vec1.keys() | vec2.keys())

            # print(intersection)
            inner_sum = 0
            for word in all_words:
                if word in vec1 and word in vec2:
                    if (vec1[word] - vec2[word]) != 0:
                        inner_sum += math.pow(vec1[word] - vec2[word], 2)
                elif word in vec2:
                    inner_sum += math.pow(vec2[word], 2)
                elif word in vec1:
                    inner_sum += math.pow(vec1[word], 2)
            srt_sum = math.sqrt(inner_sum)

            cosine_scores.append([counter, counter2, round(srt_sum)])
            counter2+=1
        counter+=1
    return cosine_scores

cos_values = get_Eucilian()
import pprint as pp
pp.pprint(cos_values)



