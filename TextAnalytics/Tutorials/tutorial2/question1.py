'''Question 1 - Use NLTK package, normalise text file with tokenizer method,
    Use the postagger and look for inaccuracies'''

# Imports
import nltk


# list_words = ["Hello", "lower", "Upper"]
# list_words_lower = [ word.lower for word in list_words]

'''
Another method to read in from file
file = open("directory/to/file")
raw_text = file.read()
raw_text
'''

# Part a

# Function to read from text file and return string
def read_text_from_file(file_path_name):
    # Open the file and read in the text
    with open(file_path_name) as file:
        text = file.read()
        file.close()
    return text


paragraph = read_text_from_file("nltk_file.txt")

# normalise the data by making lower case
paragraph = paragraph.lower()

token_words = nltk.word_tokenize(paragraph)

print(token_words)

# Oddities
# Speech marks are seperated from the words they follow into there own
# We'll is split into we and 'll and It's is split into it and 's
# Yet 'O'Kelly' is kept as one word
# hyphan words are kept together eg. ice-skate
# U.C.C was also kept as one word, yet when
# The link http://nltk.org/ was split into 3 'words'


token_words = nltk.pos_tag(token_words)
print(token_words)






