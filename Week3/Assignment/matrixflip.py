def matrixflip(m,d):
    l = m[:]
    if d == 'h':
        for i in l:
            i.reverse()
    elif d == 'v':
        l.reverse()
    else:
        return m
    return(l)