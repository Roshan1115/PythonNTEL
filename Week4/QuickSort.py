def QuickSort(A,L,R):
    if R-L <= 1:
        return()
    yellow = L+1
    for green in range(L+1, R):
        if A[green] <= A[L]:
            A[green],A[yellow] = A[yellow],A[green]
            yellow = yellow + 1

    #Move Pivote to the centere
    A[L],A[yellow-1] = A[yellow-1],A[L]
    #The recursion call
    QuickSort(A,L,yellow-1)
    QuickSort(A,yellow,R)
    