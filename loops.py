def index_of_by_index(word, mylist, index):
    for i in range(index,len(mylist)):
        if mylist[i] == word:
            return i 
    return -1

def index_of_empty(mylist):
    for i,item in enumerate(mylist):
        if item == "":
            return i 
    return -1

def index_of(word, mylist):
    index = 0
    for item in mylist:
        if item == word:
            return index 
        index += 1
    return -1

def put(word, mylist):
    for i,item in enumerate(mylist):
        if item == "":
            mylist [i] = word
            return i 
    return -1

def remove(word, mylist):
    count = 0
    for index, item in enumarate(mylist):
        if item == word:
            mylist[index] =""
            count += 1
    return count
