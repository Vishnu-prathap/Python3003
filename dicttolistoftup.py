dict1 = {'A': 10, 'B': 12, 'C': 31}
def dictolist(dict1):
  list1 = [(k,dict1[k]) for k in dict1]
  return list1

print(dictolist(dict1))
