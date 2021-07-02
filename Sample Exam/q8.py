def repeated(l):
    myL = l[:]
    helperList = []
    count = 0
    for i in range(len(myL)):
        for j in range(i+1,len(myL)):
            if myL[i] not in helperList:
                if myL[i] == myL[j]:
                    count += 1
                    helperList.append(myL[i])
                    break
    return(count)

