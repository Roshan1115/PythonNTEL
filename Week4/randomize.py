import random

def ramdomize(l):
    for i in range(len(l)//2):
        j = random.randrange(0,len(l),1)
        k = random.randrange(0,len(l),1)
        l[j],l[k] = l[k],l[j]
        
mylist = [1,2,4,3,6,5]
ramdomize(mylist)
print(mylist)