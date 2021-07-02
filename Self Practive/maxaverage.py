def aboveaverage(l):
    d_score = {}
    d_count = {}
    d_avgscore = {}
    player = []
    finalList = []

    for i in range(len(l)-1):
        count = 1
        total_score = l[i][1]
        for j in range(i+1, len(l)):
            if l[i][0] == l[j][0] and l[i][0] not in player:
                count = count + 1
                total_score = total_score + l[j][1]
                d_count[l[i][0]] = count
                d_score[l[i][0]] = total_score
                player.append(l[i][0])
    
    for i in range(len(l)):
        if l[i][0] not in player:
            d_count[l[i][0]] = 1
            d_score[l[i][0]] = l[i][1]

    for i in d_score.keys():
        d_avgscore[i] = d_score[i]/d_count[i]

    maxScore = max(d_avgscore.values())
    for i in d_avgscore.keys():
        if d_avgscore[i] == maxScore:
            finalList.append(i)

    finalList = sorted(finalList)
    
    return(finalList)


# myList = [('Kohli',73), ('Ashwin', 33), ('Kohli', 7), ('Pujara', 22), ('Ashwin', 47)]
print(aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',22),('Ashwin',47)]))