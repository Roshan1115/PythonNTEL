from itertools import permutations
st=['a','b','c','d','e','f','g','h','i','j']
y=tuple('ghadbicefj')  
#you can take any word into 'y' using input function, dynamically to find the next word.
st=permutations(list(st))
st=sorted(st)
ind=st.index(y)
print(''.join(st[ind-1]))

#ghadbicefj