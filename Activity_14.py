def input_dimensions():
    num = int(input("Enter the values of length, breadth and Height of tromboloid: "))
    
    return int(num.split())
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
    l = input_dimensions()
    b = input_dimensions()
    h = input_dimensions()
    k = valk(l,b,h)
    volume = vol(l,b,h,k)
    print("The volume of the trombolod is: ",volume)
    r = radius(volume)
    print("Radius of sphere with same volume as tromboloid: ",r)
    
    
main()

