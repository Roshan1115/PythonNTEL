def decreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(l[0] > l[1] and decreasing(l[1:]))

print(decreasing([3,18,4]))