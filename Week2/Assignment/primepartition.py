def PrimeCheck(num):    # cheking for prime number
    if (num == 0 or num == 1):
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if (num%i == 0):
            return False
        elif i == num-1:
            return True

def primepartition(m):    # Checking for partitionability
    if m <= 2:      # number less than 2cannot be partitioned into prime numbers
        return False
    Prime_upto_number = []
    for i in range(2, m-1):
        if(PrimeCheck(i) == True):
            Prime_upto_number.append(i)
    for p in Prime_upto_number:
        q = m - p
        if(q in Prime_upto_number):
            return True
    else:
        return False

a = int(input("Enter the number: "))
print(primepartition(a))
