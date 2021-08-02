a = int(input("Enter value:"))
b = int(input("Enter value:"))
c = int(input("Enter value:"))
d = int(input("Enter value:"))
e = int(input("Enter value:"))
list_sum = [a,b,c,d,e]
sum = 0
for i in list_sum:
    sum =sum +int(i)
print(sum)    
//2-Found an another way to take user input and sum    
lst=[]
n = int(input("Enter the number of elements in the list\n"))
for i in range(0,n):
    ele = int(input("Enter the number\n"))
    lst.append(ele)
print(lst)    
sum = 0
for i in lst:
    sum = sum +int(i)
print(sum)    
