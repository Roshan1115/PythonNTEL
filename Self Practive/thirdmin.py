def thirdmin(l):
    (mymin, mysecondmin, mythirdmin) = (1000000, 1000000, 1000000)
    for i in range(len(l)):
        if l[i] < mymin:
            mymin = l[i]
    for i in range(len(l)):
        if l[i] < mysecondmin and l[i] > mymin:
            mysecondmin = l[i]
    for i in range(len(l)):
        if l[i] < mythirdmin and l[i] > mysecondmin:
            mythirdmin = l[i]

    return(mythirdmin)

print(thirdmin([4,1,3,2]))
