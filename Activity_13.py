def input_num():
    num = int(input("Enter a number "))
    return num
def checkforprime(num):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                return num
def main():
    a = input_num()
    c = checkforprime(a)

main()
