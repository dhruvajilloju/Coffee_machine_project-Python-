from multiprocessing.spawn import spawn_main

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
""""👉 a) Check if ingredients are enough
Compares recipe requirements to available resources."""
def is_resource_sufficient(order_ingredients):
    """returns true when the order can be made else false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

"""b) Process coins 🪙"""
def process_coins():
    """returns the total calculated from the coins inserted"""
    print("pls insert coins")
    total=int(input("how many quarters?:"))*0.25
    total+=int(input("how many dimes?:")) * 0.1
    total+=int(input("how many nickles?:")) * 0.05
    total+=int(input("how many pennies?:")) * 0.01
    return total

"""c) Handle payment"""
def is_transactions_success(money_received,drink_cost):
    """returns true when the payment is successful else false"""
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is ur change ${change}")
        global money
        money+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

"""d) Make the coffee ☕✨"""
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_name}☕😉")

"""Main Loop (Machine running)"""
is_on =True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transactions_success(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


