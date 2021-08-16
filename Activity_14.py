def input_dimensions():
    num = input("Enter the values of length, breadth and Height of tromboloid: ")
    x = num.split()
    m = [float(ele) for ele in x]#An element is to be converted into float, it searches for element in x(old list)
    return m
    
def valk(m):
    k = m[0]**2+m[1]**2+m[2]**2
    return k

def vol(m,k):
    v = ((m[1]**2)*(m[2]**2))/(k**1/2)
    return v

def radius(v):
    r = ((v*(3/4))/3.14)**(1/3)
    return r

def main():
    
    l = input_dimensions()
    k = valk(l)
    volume = vol(l,k)
    print("The volume of the trombolod is: ",volume)
    r = radius(volume)
    print("Radius of sphere with same volume as tromboloid: ",r)
    
main()


