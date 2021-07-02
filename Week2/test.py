def f(x,y):
    x = "kaleidoscope"
    y = ""
    for i in range(len(x)-1,-1,-2):
        y = x[i] + y
    return(y)

x = 'r'
y = 'b'
print(f(x,y))