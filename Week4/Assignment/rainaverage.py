# def rainaverage(l):
#     newlist = l[:]
#     i = 0
#     cityCount = 1
#     thirdList = []
#     while i < len(newlist):
#         element = newlist[i]
#         city = element[0]
#         rain = element[1]
#         totalrain = rain
#         if i != len(newlist)-1:
#             for j in newlist[i+1:]:
#                 print(i,j)
#                 scndelelement = j
#                 scndcity = scndelelement[0]
#                 scndrain = scndelelement[1]
#                 if city == scndcity:
#                     totalrain = rain + scndrain
#                     cityCount = cityCount + 1
#                     # del j

#         ar = totalrain/ cityCount
#         ar = float(ar)
#         t = (city,ar)
#         thirdList.append(t)
#         i = i+1
#     return(thirdList)
    

def rainaverage(l):
    dict1={}
    final=[]
    for tup in l:
        if tup[0] in dict1:
                dict1[tup[0]].append(tup[1])
        else:
                dict1[tup[0]]=[tup[1]]

    for c in dict1:
        ar=sum(dict1[c])/len(dict1[c])
        ar = float(ar)
        final.append(tuple([c,ar]))
        final.sort()
    return final



print(rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)]))
# rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
print(rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)]))
        


        
        