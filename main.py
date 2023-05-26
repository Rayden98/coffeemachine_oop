from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Declaring the objects
my_menu = Menu()

maker = CoffeeMaker()
money_transaction = MoneyMachine()

again = True
while again:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
# 1 print report
    if choose == "report":
        report = maker.report()
        print(report)
    if choose == "off":
        again = False
# 2 check resources sufficient?
    drink = my_menu.find_drink(choose)
    check = maker.is_resource_sufficient(drink)
    if not check:
        continue
# 3 process coins
# 4 check transaction successful?
    cost = drink.cost
    payment = money_transaction.make_payment(cost)

# 5 make coffee
    order = my_menu.find_drink(choose)
    make_coffee = maker.make_coffee(order)


