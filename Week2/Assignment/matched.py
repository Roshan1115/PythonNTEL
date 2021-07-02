def matched(s):
    counter = 0
    i = 0
    while(counter >= 0 and i < len(s)):
        if(s[i] == "("):
            counter = counter + 1
        if(s[i] == ")"):
            counter = counter - 1
        i = i + 1
    if(counter == 0):
        return True
    else:
        return False

a = input("Enter string: ")
print(matched(a))