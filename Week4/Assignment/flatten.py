result =[]
def flatten(l):
    for i in l:
        if listtype(i):
            flatten(i)
        else:
            result.append(i)
    return(result)

def listtype(l):
  return(type(l) == type([]))

# print(flatten([1,2,[3],[4,[5,6]]]))
# print(flatten([1,2,3,(4,5,6)]))
