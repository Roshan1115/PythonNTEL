def insertionsort(LIST):
    if len(LIST) <= 1:
        return(LIST)
    for i in range(1, len(LIST)):
        position = i
        while (LIST[position] < LIST[position-1] and position-1 >=0):
            LIST[position-1], LIST[position] = LIST[position], LIST[position-1]
            position = position - 1
    return (LIST)

mylist = list(range(100,1,-1))
print(insertionsort(mylist))