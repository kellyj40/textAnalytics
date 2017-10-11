import pickle
# Open old dictionary of words
with open('bloomberg_news.pkl', 'rb') as f:
    old_dict_of_words = pickle.load(f)
    f.close()

def soft_dictionary(dict_of_words):
    array = [["one", 0], ["two", 0], ["three", 0], ["four", 0], ["five", 0]]
    for key in dict_of_words:
        number_of_appearences = dict_of_words[key]
        if number_of_appearences > array[0][1]:
            array[4] = array[3]
            array[3] = array[2]
            array[2] = array[1]
            array[1] = array[0]
            array[0] = [key, number_of_appearences]
        elif number_of_appearences > array[1][1]:
            array[4] = array[3]
            array[3] = array[2]
            array[2] = array[1]
            array[1] = [key, number_of_appearences]
        elif number_of_appearences > array[2][1]:
            array[4] = array[3]
            array[3] = array[2]
            array[2] = [key, number_of_appearences]
        elif number_of_appearences > array[3][1]:
            array[4] = array[3]
            array[3] = [key, number_of_appearences]
        elif number_of_appearences > array[4][1]:
            array[4] = [key, number_of_appearences]
    return array

print(soft_dictionary(old_dict_of_words))