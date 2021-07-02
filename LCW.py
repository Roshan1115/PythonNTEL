def LCW(u,v):
    MyList = [None]*(len(u)+1)
    # print(MyList)
    for r in range(len(u)+1):
        MyList[r][len(v)] = 0
        # print(MyList)
    for c in range(len(v)+1):
        MyList[len(u)][c] = 0

    maxLCW = 0
    for c in range(len(v)-1, -1, -1):
        for r in range(len(u)-1, -1, -1):
            if u[r] == u[c]:
                MyList[r][c] = 1 + MyList[r+1][c+1]
            else:
                MyList[r][c] = 0
            if MyList[r][c] > maxLCW:
                maxLCW = MyList[r][c]
    return(maxLCW)

u = "SECRET"
v = "BISECT"

print(LCW(u,v))