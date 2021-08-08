def input_number():
    num = int(input("Enter a number"))
    return num
def add(a,b):
    return a+b
def display(a,b,c):
    print(f"{a}+{b} = {c}")
def main():
    a = input_number()
    b = input_number()
    summation = add(a,b)
    display(a,b,summation)
main()
