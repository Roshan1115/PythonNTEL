
#My Version of Selection sort

def selectionsort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if(l[i] > l[j]):
                (l[i], l[j]) = (l[j], l[i])
    return(l)