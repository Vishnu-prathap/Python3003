lst = input("Enter the numbers:")
numo = lst.split()
print(numo)
num1 = numo[0:3]
print(num1)
num1[0] = 0
num1[2] = 0
print(num1)
print(numo[::-1])

