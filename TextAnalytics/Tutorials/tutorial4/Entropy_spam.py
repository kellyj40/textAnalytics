import math
import nltk

spam = ["Try out microsofts new online platform system.",
        "Apply online now to our graduate program",
        "Mark was an intern in 2015, and has never looked bask...Apply online, closing date end of November",
        "Graduate positions in software development roles starting in June. Apply online before November",
        "Join Microsoft today and be in with a chance of 100 euro... Sign up today online",
        "Morgan Stanley, lots of IT graduate roles available, apply online before November",
        "Try out JP. Morgans new online process system to apply for graduate and intern jobs",
        "Applying to Microsoft graduate job has never been eaiser, visit and apply online before November",
        "Graduate roles for Morgan Stanley to be online in November",
        "Apply to Microsoft todday online."]


random_tweets = [
    "Two years ago today, Shane Long scored this famous goal as Ireland beat the world champions",
    "Breaking: Michel Barnier says EU and UK govt have reached 'disturbing' deadlock on #Brexit bill - doesn't back moving to next stage of talks",
    "Looking for decent book recommendations as have 18 hours of travel time to fill and I don't sleep on planes!",
    "What a performance by the lads. Fully deserved that win. Proud to captain",
    "Ever noticed how fast gov moves when it's power is at risk, and how slow it moves when the people stand to gain power?",
    "I took a little drive tonight to see what I could see.. I saw this..",
    "It's a mad idea that shouldn't work....economics and comedy... but its does! Here's our full program",
    "Bored of the budget already?Interested in alternative ways of running the economy. Don't miss this with",
    "Can't wait for November  9th to 12th and one of our favourite festivals"
]

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# Get rid of stop words
spam = [word.lower() for word in spam if word not in stop_words]
random_tweets = [word.lower() for word in random_tweets if word not in stop_words]

def entropy(labels):
    arr = []
    # split sentences into their words
    for sentence in labels:
        words = sentence.split(" ")
        arr.append(words)

    # make 2d array into 1d
    arr2 = [j for i in arr for j in i]

    # get the number of occurances of each word in the array
    freq_dist = nltk.FreqDist(arr2)
    # get the propability --> number_of_occurances/total_number_of_words
    prob = [freq_dist.freq(l) for l in freq_dist]

    return -sum(p*math.log(p, 2) for p in prob)

# Print results
print("Spam tweets: " + str(entropy(spam)))
print("Normal tweets: " + str(entropy(random_tweets)))
mix_tweets = spam[:5] + random_tweets[5:]
print("Mix tweets: " + str(entropy(mix_tweets)))



