b = float(input("Enter the breadth of tromboloid:\n"))

h = float(input("Enter the height of tromboloid:\n"))

l = float(input("Enter the lenght of tromboloid:\n"))

k = l**2+b**2+h**2

v = ((b**2)*(h**2))/(k**1/2)
print("The volume of tromboloid is :",v)
r = (v*(3/4))/3.14
#print(r)
r1 = r**(1/3)
print("Radius of sphere with same volume as troboloid is: ",r1)


