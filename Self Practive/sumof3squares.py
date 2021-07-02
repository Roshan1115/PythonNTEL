def sumof3squares(n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            for k in range(1,n-1):
                if (i**2 + j**2 + k**2 == n):
                    return True
    return False

a = int(input('enter the nubert : '))
print(sumof3squares(a))