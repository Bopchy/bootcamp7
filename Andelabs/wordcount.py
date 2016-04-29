wordslist = wordlst.split()

dict_ = {}

for word in wordslist:
    if word.isdigit():
        word = int(word)
    if word in dict_:
        dict_[word] = dict_[word] + 1
    else:
        dict_[word] = 1

return dict_