import math
import nltk

spam = ["Ever iphone wondered how to join iphone run your own Twitter chat? Here are iphone some tips on how iphone to plan, promote, and execute.",
        "Go beyond iphone join the conventional, iphone insane and dabbling. Here are 5 ways iphone to rethink how you do iphone analytics.",
        "The future join  iphone of mixing & mastering is here. Get to know the new iphone Ozone iphone 8 & Neutron 2.",
        "Get iphone the iphone most out of the latest iphone #MicrosoftEDU tools with videos, online demos, and iphone more from Back to School LIVE!",
        "Two iphone investment iphone bank leaders discuss the future of investing. Learn more..",
        "Today is join iphone the day! Learn from SAP Cloud Platform experts how to iphone accelerate in your build of cloud applications. #SCP",
        "For iphone just €35 a month for the first 6 iphone months, sign iphone up to unlimited broadband and get iphone all this free ",
        "Improve iphone the quality of care join in your iphone services with our Sit&See programme, a iphone primary preventative strategy.",
        "Join us iphone iphone live from iphone the #wdayrising show floor iphone to hear about the iphone integration between Adobe Sign and",
        "Join ODPi, Hortonworks iphone, join IBM & ING for iphone an iphone exploration of Data Governance iphone in this Linux Foundation iphone webinar!"]


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
spam = [word for word in spam if word not in stop_words]
random_tweets = [word for word in random_tweets if word not in stop_words]

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

print("Spam tweets: " + str(entropy(spam)))
print("Normal tweets: " + str(entropy(random_tweets)))
mix_tweets = spam[:5] + random_tweets[5:]
print("Mix tweets: " + str(entropy(mix_tweets)))



