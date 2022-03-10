from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

working = True
menu = Menu()
my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while working :
  items = Menu().get_items()
  question = input(f"What would you like? ({items}): ")
  if question == "off" : 
    working = False
    break
  elif question == "report" :
    my_money_machine.report()
    coffee_maker.report()
  else :
    drink = Menu().find_drink(question)
    if coffee_maker.is_resource_sufficient(drink) and  my_money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
  
      
      