def input_system():
    sys = input("Enter the system,database,username and password\n")#Accepts input
    s = sys.split()#Makes a list by splitting
    t = tuple(s)#Converts into list into tuple
    return t
def main():
    s = input_system()
    print(('System',s[0]),('Database',s[1]),('Username',s[2]),('Password',s[3]))

main()    
    
