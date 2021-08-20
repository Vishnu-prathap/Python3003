def ipt():
    a = input("Enter the system, database ,username and password\n")
    return a
def stringTo_tupleconverter(a):
    x = a.split(";")
    lst = []
    for i in x:#for goes through each element in its order in list 
        ele = i.split("=")
        lst.append(tuple(ele))
    return lst
    
def main():
    a = ipt()
    b = stringTo_tupleconverter(a)
    print(b)
    
main()

