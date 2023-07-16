def input_number_of_numbers():
  n = int(input("Enter the number (n) to be added\n"))
  return n

def input_numbers(a):
  numbers = []
  numbers = [int(a) for a in input("Enter the numbers\n").split(" ")]
  return numbers

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


