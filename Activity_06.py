lst = input("Enter the numbers:")
num = lst.split()
print(num)
num1 = num[0:3]
print(num1)

num[0:5]=[0,4,9,1,0]
print(num)
num[0:3] = [0,4,0]
print(num)
num.reverse()
print(num)
