
import math
def input_num():
    num = int(input("Enter a number "))
    return num

def checkforprime(num):
    flag = 1
    if num>1:
        for i in range(2,int(math.sqrt(num))):
            if (num%i)== 0:
                flag = 0
    return flag
def output(flag,num):
             
        if(flag==1):
            print(f"{num} is a prime number\n")
            
                    
        else:
            print(f"{num} is not a prime number\n")
    
    
    
def main():
    a = input_num()
    c = checkforprime(a)
    d = output(c,a)
main()

