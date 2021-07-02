def RIS(LIST):
    isort(LIST, len(LIST))
    return(LIST)

def isort(LIST, k):
    if k > 1:
        isort(LIST, k-1)
        insert(LIST, k-1)

def insert(LIST, k):
    position = k
    while (position > 0 and LIST[position] < LIST[position -1]):
        LIST[position], LIST[position-1] = LIST[position-1], LIST[position]
        position = position -1

print(RIS([3,2,6,5,7,4,3]))