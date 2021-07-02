def uncommon(l1,l2):
    result = []
    for i in l1:
        if i not in l2 and i not in result:
            result.append(i)
    for j in l2:
        if j not in l1 and j not in result:
            result.append(j)
    
    result.sort()
    return result

list1 = [2,2,4]
list2 = [1,3,3,4,5]
print(uncommon(list1,list2))