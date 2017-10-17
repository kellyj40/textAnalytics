from nltk.corpus import stopwords

# stop words to be removed
stop_words = stopwords.words('english')

base = "hurricane ophelia hits ireland and schools close"
# List of sentences
sentences = ["hurricane ophelia hits ireland and schools close",
             "hurricane ophelia misses england and work still closed",
             "storm ophelia hits ireland and schools close",
             "hurricane ophelia hits cork and houses destroyed",
             "tornado sarah hits usa and colleges close",
             "there was a hurricane in Ireland today",
             "the schools in ireland close as hurricane ophelia is to hits them"]

# Two Functions to calculate the jaccard distance
def jaccardIndex (str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float(len(set1 & set2)) / len(set1|set2)
    return round(1 - ans, 2)

# This one removes the stop words first
def jaccardIndexStops (str1, str2):
    str1 = str1.split()
    str2 = str2.split()
    # Get rid of stop words
    strings1 = [word.lower() for word in str1 if word not in stop_words]
    strings2 = [word.lower() for word in str2 if word not in stop_words]
    set1 = set(strings1)
    set2 = set(strings2)
    ans = float(len(set1 & set2)) / len(set1|set2)
    return round(1 - ans, 2)

# Showing the result on a base sentence
for sentence in sentences:
    print("Score with stop words: " + str(jaccardIndex(base, sentence)))
    print("Scores without stops: " + str(jaccardIndexStops(base, sentence)))
    print()

# Empirically show by calculating it across all the sentences
base = ["hurricane ophelia hits ireland and schools close",
        "hurricane ophelia misses england and work still closed",
        "storm ophelia hits ireland and schools close",
        "hurricane ophelia hits cork and houses destroyed",
        "tornado sarah hits usa and colleges close",
        "there was a hurricane in Ireland today"]

# Show the resutls of each sentance against one another
count = 0
dict_val = {"0": "X", "1": "Y", "2": "Z", "3": "A", "4": "B", "5": "C"}
while count < len(base):
    innerCount = 0
    while innerCount<len(base):
        if innerCount!=count:
            print("Sentence "+dict_val[str(count)]+" and "+dict_val[str(innerCount)]+" resulted in: " + str(jaccardIndex(base[count], base[innerCount])))
        innerCount += 1
    count += 1
