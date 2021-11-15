MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00
machine_money = 0.00

# FUNCTIONS START HERE

def check_resources(name):
    """Checks to determine if sufficient resources to make drink exists."""
    if name == "espresso":
        if resources["water"] < MENU[name]["ingredients"]["water"]:
            print(f"Sorry, there is not enough water. Water remaining is {MENU[name]['water']['ingredients']}"
                  f", need {resources['water']}.")
            return False
        elif resources["coffee"] < MENU[name]["ingredients"]["coffee"]:
            print(f"Sorry, there is not enough coffee. Coffee remaining is {MENU[name]['coffee']['ingredients']}"
                  f", need {resources['coffee']}.")
            return False
        else:
            return True
    elif name == "latte" or name == "cappuccino":
        if resources["water"] < MENU[name]["ingredients"]["water"]:
            print(f"Sorry, there is not enough water. Water remaining is {resources['water']}, "
                  f"need {MENU[name]['ingredients']['water']}.")
            return False
        elif resources["coffee"] < MENU[name]["ingredients"]["coffee"]:
            print(f"Sorry, there is not enough coffee. Coffee remaining is {resources['coffee']}"
                  f", need {MENU[name]['ingredients']['coffee']} .")
            return False
        elif resources["milk"] < MENU[name]["ingredients"]["milk"]:
            print(f"Sorry, there is not enough milk. Milk remaining is {resources['milk']}"
                  f", need {MENU[name]['ingredients']['milk']} .")
            return False
        else:
            return True


def check_money(drink, amount):
    """ Check to see if enough money was given for a drink"""
    if (drink == "espresso" and amount < MENU[drink]["cost"]) or (drink == "latte" and amount < MENU[drink]["cost"])\
            or (drink == "cappuccino" and amount < MENU[drink]["cost"]):
        # if not enough money, start over
        print(f"Sorry that's not enough money. Drink is ${MENU[drink]['cost']}. You gave ${amount}. Money refunded.")
        return False
    else:
        return True


def use_machine_resources(drink):
    """ Deduct resources from the machine to make the drink."""
    if drink == "latte" or drink == "cappuccino":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    elif drink == "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return resources


def check_required_change(drink, amount):
    """Check to see if change is required and return change amount if so."""
    if (drink == "espresso" and amount > MENU[drink]["cost"]) or (drink == "latte" and amount > MENU[drink]["cost"])\
            or (drink == "cappuccino" and amount > MENU[drink]["cost"]):
        return amount - MENU[drink]["cost"]
    else:
        return 0.00

# START MACHINE HERE

isMachineOn = True

while isMachineOn:
    print(""" Menu prices:
    \tespresso: $1.50
    \tlatte: $2.50
    \tcappuccino: $3.0 """)
    choice = input("What would you like to drink? ")

    # Checks if enough resource, returns True if yes, False if not
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        isSufficient = check_resources(choice)
    elif choice == "report":
        # displays the amount of resources in the machine
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {format(machine_money, '.2f')}\n")
        isSufficient = False
    elif choice == "off":
        # turn the machine off
        isMachineOn = False
        isSufficient = False
    else:
        print("Try your selection again.")
        isSufficient = False

    if isSufficient:
        print("Please insert coins.")
        quarters = float(input("how many quarters?:"))
        dimes = float(input("how many dimes?:"))
        nickles = float(input("how many nickles?:"))
        pennies = float(input("how many pennies?:"))

        quarters_total = quarters * .25
        dimes_total = dimes * .10
        nickles_total = nickles * .05
        pennies_total = pennies * .01

        money = (quarters_total + dimes_total + nickles_total + pennies_total)
        print(money)
    # Check to see if received enough money
        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            isEnoughMoney = check_money(choice, money)
        # #if sufficient money, make drink
            if isEnoughMoney:
                required_change = check_required_change(choice, money)
                if required_change > 0.00:
                    print(f"You gave ${format(money, '.2f')}. Here is ${format(required_change, '.2f')} in change.")
                    money -= required_change
                    machine_money += money
                    print("Making your drink now.")
                else:
                    machine_money += money
                    print("Making your drink now.")
                # deduct resources from the machine
                remaining_resources = use_machine_resources(choice)
                # present drink
                print(f"Here is your {choice} ☕. Enjoy!")



