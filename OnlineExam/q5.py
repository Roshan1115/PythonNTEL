def sum3cubes(n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            for k in range(1,n-1):
                if i**3 + j**3 + k**3 == n:
                    return True
    else:
        return False