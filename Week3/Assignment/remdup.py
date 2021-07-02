def remdup(l):
    if len(l) == 0:
        return []
    else:
        return removeLastOccur(l)

def removeLastOccur(l):
    AnswerList = []
    l.reverse()
    for i in l:
        if i not in AnswerList:
            AnswerList.append(i)
    AnswerList.reverse()
    return (AnswerList)

# print(remdup([1,2,3,4,5,3,5]))