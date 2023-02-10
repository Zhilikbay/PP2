def unique_list(y):
  x = []
  for a in y:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 