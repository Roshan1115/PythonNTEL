def splitsum(l):
    AnswerList = []
    pos = 0
    neg = 0
    for i in l:
        if i > 0:
            pos = pos + (i*i)
        elif i < 0:
            neg = neg + (i*i*i)
    AnswerList.append(pos)
    AnswerList.append(neg)
    return AnswerList

