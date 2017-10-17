base = ["storm ophelia hits ireland and schools close",
        "hurricane ophelia hits ireland and schools close",
        "hurricane ophelia misses england and work",
        "hurricane ophelia hits cork and houses destroyed",
        "tornado sarah hits usa and colleges close",
        "there was a hurricane in Ireland today"]




# Two Functions to calculate the jaccard distance
def dice_coefficient (str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float((2 *len(set1 & set2))) / (len(set1) + len(set2))
    return round(1 - ans, 2)

# Show the resutls of each sentance against one another
count = 0
dict_val = {"0": "X", "1": "Y", "2": "Z", "3": "A", "4": "B", "5": "C"}
while count < len(base):
    innerCount = 0
    while innerCount<len(base):
        if innerCount!=count:
            print("Sentence "+dict_val[str(count)]+" and "+dict_val[str(innerCount)]+" resulted in: " + str(dice_coefficient(base[count], base[innerCount])))
        innerCount += 1
    count += 1