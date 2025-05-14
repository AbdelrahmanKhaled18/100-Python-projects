from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    while is_on:
        choice = input(f"Welcome to the coffee machine! What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
