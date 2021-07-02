def MergeSort(A,left,right):
    if right-left <= 1:
        return(A[left:right])
    if right-left > 1:
        mid = (left + right)//2
        l = MergeSort(A,left,mid)
        r = MergeSort(A,mid,right)
        return(Merge(l,r))

def Merge(a,b):
    c,m,n = [],len(a),len(b)
    i,j = 0,0
    while i+j < m+n:
        if i == m:
            c.append(b[j])
            j = j+1
        elif j == n:
            c.append(a[i])
            i = i+1
        elif a[i] <= b[j]:
            c.append(a[i])
            i = i+1
        elif a[i] > b[j]:
            c.append(b[j])
            j = j+1
    return(c)


mylist = [6,5,4,3,2,1]
print(MergeSort(mylist,1,5))