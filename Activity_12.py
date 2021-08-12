def input_number():
    num = int(input("Enter the number"))
    return num
def compare(a,b,c):
    if (a<b)and(c<b):
        print(f"{b} is the greatest number")
    elif (c>a):
        print(f"{c} is the greatest number")
    else:
        print(f"{a} is the greatest number")
def main():
    a = input_number()
    b = input_number()
    c = input_number()
    compare(a,b,c)

main()
