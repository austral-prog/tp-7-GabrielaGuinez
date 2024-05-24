def index_of_by_index(word,mylist,index):
    for i in range(index,len(mylist)):
        if mylist[i]==word:
            return i 
    return -1

def index_of_empty(mylist):
    for i,item in enumerate(mylist)
        if item==word:
            return i 
    return -1

def index_of(word,mylist):
    for i,item in enumerate(mylist):
        if item==word:
            return i 
    return -1

def put(word,mylist):
    for i,item in enumerate(mylist):
        if item=="":
            list[1]=word
            return i 
    return -1

def remove(word,mylist):
    count=0
    for i,item in enumerate(mylist)
        if item==word:
            mylist[i]==""
            count+=1
        return count
    return -1
