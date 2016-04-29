# wordslist = wordslist.split()

# dict_ = {}

# for word in wordslist:
#     if word.isdigit():
#         word = int(word)
#     if word in dict_:
#         dict_[word] = dict_[word] + 1
#     else:
#         dict_[word] = 1

# return dict_

# split() returns a list of all the words in a
# string, using specified str or whitespace as 
# separator  

def words(sentence):
    sentence = sentence.split()
    # splits a string of items in a sentence words
    dict_ = {} # initializing empty dict
    # empty dict is used for storing the recurring numbers 
    for word in sentence: # loops through content of sentence
        if word.isdigit(): # isdigit() checks if a string 
        # consists of digits only
            word = int(word) # counts digit as one word 
        if word in dict_: # loop for adding words into dictionary
            dict_[word] = dict_[word] + 1
        else:
            dict_[word] = 1

    return dict_