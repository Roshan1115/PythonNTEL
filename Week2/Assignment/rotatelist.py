def rotateOne(l):
    first_element = l[0]
    for i in range(0, len(l)):
        if(i == len(l)-1):
            l[i] = first_element
        else:
            l[i] = l[i + 1]
    # return(l)

def rotatelist(LIS,k):
    l = LIS[:]
    if(k <= 0):
        return(LIS)
    for i in range(1, k+1):
        rotateOne(l)
    return(l)

print(rotatelist([1,2,3,4,5],3))