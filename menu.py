class menu:
  def __init__(self,item,price):
    self.item = item
    self.price = price

  def dictmenu(self):
    #print("The items in the menu of Brahmins Cafe is mentioned below along with the prices\n")

    self.menu = {self.item:self.price}
    return self.menu

a = menu("Idli",10)
b = menu("Vada",20)
print(a.dictmenu(),b.dictmenu())

