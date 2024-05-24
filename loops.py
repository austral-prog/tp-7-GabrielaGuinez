def index_of_by_index(word,list,index):
    for i in range(index,len(list)):
        if list[i]==word:
            return i 
    return -1

def index_of_empty(list):
    for i,item in enumerate(list)
        if item==word:
            return i 
    return -1

def index_of(word,list):
    for i,item in enumerate(list):
        if item==word:
            return i 
    return -1

def put(word,list):
    for i,item in enumerate(list):
        if item=="":
            list[1]=word
            return i 
    return -1

def remove(word,list):
    count=0
    for i,item in enumerate(list)
        if item==word:
            list[i]==""
            count+=1
        return count
    return -1
