from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like from ({options})").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        #To get report of money and remaining coffee
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # To get resources and make payment, give change back for coffee 
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): 
                coffee_maker.make_coffee(drink)
