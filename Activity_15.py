def input_str():
    st = input("Enter a list of strings")
    s = st.split()
    return s
def sorting(s):
    s.sort()#doesnt return any value,and default value returned is "none"
def main():
    a = input_str()
    print(a)
    sorting(a)
    print(a)
    
main()


def input_str():
    st = input("Enter a list of strings")
    s = st.split()
    return s
def sorting(s):
    x = sorted(s)
    return x
def main():
    a = input_str()
    print(a)
    x=sorting(a)
    print(x)
main()
