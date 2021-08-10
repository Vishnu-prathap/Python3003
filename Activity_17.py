def input_tup():
    t = input("Enter the system, database, username and password\n")
    return t.split()
def change(t):
    l = list(t)
    return l
def main():
    s = input_tup()
    l = change(s)
    print("System :",l[0],"Database :", l[1],"Username :",l[2],"Password :",l[3])
main()
