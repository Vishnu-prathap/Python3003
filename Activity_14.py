def input_dimensions():
    num = input("Enter the values of length, breadth and Height of tromboloid: ")
    x = num.split()
    l,b,h = [float(ele) for ele in x]#An element is to be converted into float, it searches for element in x(old list) with list unpacking
    return l,b,h
    
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
    
    l,b,h = input_dimensions()
    k = valk(l,b,h)
    volume = vol(l,b,h,k)
    print("The volume of the trombolod is: ",volume)
    r = radius(volume)
    print("Radius of sphere with same volume as tromboloid: ",r)
    
main()


