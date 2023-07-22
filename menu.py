def dictmenu():
  print("The items in the menu of Brahmins Cafe is mentioned below along with the prices\n")
  menu = {
      "Idli": 10,
      "Vada": 20,
      "Kharabath": 20,
      "Kesaribath": 20
  }
  return menu

def numberofitems(a):
  n = int(input("Enter the number of items required\n"))
  total_cost= []
  #total_items = []
  for i in range(n):  
    i = input("Enter item name ")
    print("The price of the item is",a[i],"Rupees.")
    total_cost.append(a[i])
  return total_cost

def fixed_menu():
  a = dictmenu()
  print(a)
  b= numberofitems(a)
  print("The sum total of the all the items ordered is",sum(b))
 

fixed_menu()
