lst = []
n = int(input("Enter the number of elements for list\n"))
for i in range(0,n):
    ele = int(input("Enter the number\n"))
    lst.append(ele)
print(lst)#Print list
print(lst[0:3])#print list's first 3 elements
lst[0:5] = [0,4,9,1,0]
print(lst)
lst[0:3] = [0,4,0]
print(lst)#print list with the first 3 elements changes
print( lst[::-1])#Print list in reverse manner
