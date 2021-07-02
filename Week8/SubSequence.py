Sequence_lenght = int(input())
SequenceList = []
SequenceList.append(Sequence_lenght)

for i in range(Sequence_lenght):
    inputNumber = int(input())
    SequenceList.append(inputNumber)

myDict = {}

for i in range(len(SequenceList)):
    myDict[SequenceList[i]] = []
    for j in range(i+1, len(SequenceList)):
        if SequenceList[j] % SequenceList[i] == 0:
            myDict[SequenceList[i]].append(SequenceList[j])

myDict[SequenceList[-1]] = []
maxList = []

def find_connection(n,localmax):
    if len(myDict[n]) < 1:
        return
    if len(myDict[n]) >= 1:
        localmax = localmax + 1
        maxList.append(localmax)
        for i in myDict[n]:
            find_connection(i,localmax)

for i in SequenceList:
    find_connection(i,1)

print(max(maxList))

