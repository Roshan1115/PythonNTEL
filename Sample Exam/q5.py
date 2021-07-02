def perfect(n):
    c = []
    for i in range(1,n//2+1):
        if(n%i == 0):
            c.append(i)
    if sum(c) == n:
        return (True)
    else:
        return(False)

a = int(input("enter the number: "))
print(perfect(a))
