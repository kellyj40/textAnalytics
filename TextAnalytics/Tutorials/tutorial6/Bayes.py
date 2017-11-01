import nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'last_letter': word[-1]}

def gender_features(word):
    return {'last_two_letter': word[-2:]}

def gender_features(word):
    return {'first_letter': word[0]}

def gender_features(word):
    return {'first_two_letter': word[:1]}

def gender_features(word):

    if len(word) > 3 and len(word) < 7:
        v = ['a', 'o', 'u', 'i', 'e']
        vowels = [char_val for char_val in word if char_val in v]
        return {'length': len(vowels)}

    if len(word) <= 3:
        return {'last_letter': word[0]}

    return {'last_letter': word[-1]}


male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
#entries are    ({'last_letter': 'g'}, 'male')
train_set, test_set = featuresets[500:], featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))

ans1 = classifier.classify(gender_features('Mark'))
ans2 = classifier.classify(gender_features('Precilla'))

print(ans1)
print(ans2)

# classifier.show_most_informative_features(5)
# print(nltk.classify.accuracy(classifier, test_set))





