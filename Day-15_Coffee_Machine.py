MENU = {
    "espresso" :{
        "ingredients" : {
            "water" : 50,
            "coffee" : 18
        },
        "cost" : 1.5
    },
    "latte" :{
        "ingredients" : {
            "water" : 200,
            "coffee" : 24,
            "milk" : 150
        },
        "cost" : 2.5
    },
    "cappuccino" :{
        "ingredients" : {
            "water" : 250,
            "coffee" : 24,
            "milk" : 100
        },
        "cost" : 1.5
    }
}
is_coffee_machine_on = True
profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}

def ask_flavour():
    usr_input = input("What would you like? (espresso/latte/cappuccino/off): ")
    return usr_input

def check_inserted_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return ((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies))
    
def check_for_resources(flavour):
    global is_coffee_machine_on
    for ing in MENU[flavour]["ingredients"]:
        if resources[ing] < MENU[flavour]["ingredients"][ing]:
            print(f"Sorry there is not enough {ing}, Money refunded.")
            return False
    return True
    
def change(flavour, total_amount):
    if total_amount - MENU[flavour]["cost"] < 0:
        print("Sorry, that's not enough. Money refunded.")
        return False, 0
    else:
        return True, total_amount - MENU[flavour]["cost"]

def coffee_machine():
    global profit
    global resources
    flavour = ask_flavour()
    if flavour == "report":
        for resource in resources:
            if resource == "coffee":
                print(f"{resource.capitalize()} : {resources[resource]}g")
            else:
                print(f"{resource.capitalize()} : {resources[resource]}ml")
        print(f"Money : {profit}")
    elif flavour == "off":
        global is_coffee_machine_on
        is_coffee_machine_on = False
    else:
        inserted_money = check_inserted_money()
        change_bck, amt_bck = change(flavour, inserted_money)
        if change_bck:
            res = check_for_resources(flavour)
            if res:
                for ing in MENU[flavour]["ingredients"]:
                    resources[ing] -= MENU[flavour]["ingredients"][ing]
                profit += MENU[flavour]["cost"]
                print(f"Here is ${amt_bck} in change.")
                print(f"Here is your {flavour}, Enjoy!")
            
while is_coffee_machine_on:
    coffee_machine()