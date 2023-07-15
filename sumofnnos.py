def input_number_of_numbers():
  n = int(input("Enter the number (n) to be added\n"))
  return n

def input_numbers(a):
  lst = []
  for i in range(0,a):
    nos = int(input("Enter the number\n"))
    lst.append(nos)
  return lst

def sumofinputnos(b):
  sum = 0
  for i in b:
    sum = sum +i
  return sum
def main():
  a = input_number_of_numbers()
  b = input_numbers(a)
  c = sumofinputnos(b)
  print("The sum of the",a,"numbers =",c)
  return

main()

