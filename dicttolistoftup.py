dict = {'A': 10, 'B': 12, 'C': 31}


 
def dicttolist(dict):
  list1 = []
  for i in dict:
    k = (i, dict[i])
    list1.append(k)
  return list1

a = dicttolist(dict)
print(a)
