def sublist(l1,l2):
    lenL1 = len(l1)
    for i in range(len(l2)):
        if l1[:] == l2[ i : (i+len(l1)) ]:
            return(True)
    else:
        return(False)

print(sublist([2,2,3],[2,2,3,4,5]))