def input_theta():
  theta = float(input("Enter the angle for whose sin is to be calculated (in radians)\n"))
  return theta

def factorial(n):
  fac = 1
  for i in range(1,n+1):
    fac=fac*i
  return fac

def sinxvalue(n,theta,sum):
  sum = 0
  sign = 1 
  for i in range(1,n):
    sum = sum + sign*(theta**(2*i-1)/factorial(2*i-1))
    sign = (-1)*sign
  return sum

def main():
  n = 10 
  a = input_theta()
  b = sinxvalue(n,a,sum)
  print("The value of sinx = ",b)
  return 

main()
