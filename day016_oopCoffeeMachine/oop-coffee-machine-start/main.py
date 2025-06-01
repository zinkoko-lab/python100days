from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from clear import clear_screen

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
items = menu.get_items()
is_on = True

clear_screen()
while is_on:
    # 1.Prompt user by asking “​What would you like?(espresso/latte/cappuccino/):​
    choice = input(f"What would you like?({items}): ").lower().strip()

    # 2.Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == "off":
        is_on = False

    # 3.Print report.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        # 5. Check the order is in menu.
        item = menu.find_drink(choice)
        if item:
            # 6.Check resource sufficient?
            can_make = coffee_maker.is_resource_sufficient(item)
            if can_make:
                while True:
                    try:
                        # 7.Process coins and Check transaction successful?
                        if money_machine.make_payment(item.cost):
                            # 8.Make Coffee
                            coffee_maker.make_coffee(item)
                        break
                    except ValueError:
                        print(
                            "Invalid coins are detected. Money refunded and try again from start."
                        )

clear_screen()
