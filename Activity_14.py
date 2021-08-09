def input_num():
    num = float(input("Enter the number: "))
    return num
def valk(l,b,h):
    k = l**2+b**2+h**2
    return k
def vol(l,b,h,k):
    v = ((b**2)*(h**2))/(k**1/2)
    return v
def radius(v):
    r = ((v*(3/4))/3.14)**(1/3)
    return r
def main():
    print(" Lenght: ")
    l = input_num()
    print(" Breadth: ")
    b = input_num()
    print("height: ")
    h = input_num()
    k = valk(l,b,h)
    volume = vol(l,b,h,k)
    print("The volume of the trombolod is: ",volume)
    r = radius(volume)
    print("Radius of sphere with same volume as tromboloid: ",r)
    
    
main()
