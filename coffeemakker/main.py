from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_item = MenuItem()
c_maker = CoffeeMaker()
vend = MoneyMachine()
is_on = True

# TODO Print Report
vend.report()
c_maker.report()

# TODO Check Resources Sufficient

# TODO Process Coins

# TODO Check Transaction Successful

# TODO Make Coffee

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        c_maker.report()
        vend.report()
    else:
        drink = menu.find_drink(choice)
        if c_maker.is_resource_sufficient(drink) and vend.make_payment(drink.cost):
            c_maker.make_coffee(drink)