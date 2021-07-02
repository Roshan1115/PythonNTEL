inputdata = input()
inputList = []

while inputdata:
    inputList.append(inputdata)
    inputdata = input()

for i in range(0,len(inputList),2):
    print(inputList[i])

for j in range(1,len(inputList),2):
    print(inputList[j])

