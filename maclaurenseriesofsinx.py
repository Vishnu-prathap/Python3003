n = 10 
sum = 0
sign = 1 

def input_theta():
  theta = float(input("Enter value of X\n"))
  return theta

def factorial(n):
  fac = 1
  for i in range(1,n+1):
    fac=fac*i
  return fac

def sinxvalue(n,sign,theta,sum):
  for i in range(1,n):
    sum = sum + sign*(theta**(2*i-1)/factorial(2*i-1))
    sign = (-1)*sign
  return sum

def main():
  a = input_theta()
  b = sinxvalue(n,sign,a,sum)
  print(b)
  return 

main()

