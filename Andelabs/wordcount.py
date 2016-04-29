def word_count(string):
    words = string.split()  or unicode(string) #split into list
    count = {}
    for word in words:     
        if word in count:  
            count[word] += 1
        else:
            count[word] = 1
        #if type(string) == type(unicode):
            #count[word] += 1
    for i in count:
        print i, ":", count[i]