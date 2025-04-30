# Function to display the main menu options
def print_menu():
    print("\nWelcome to the Coffee Machine!\n")
    print("Please select an option:\n")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Report")
    print("5. Exit\n")

# Menu dictionary containing drink recipes and their cost
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

# Initial resources available in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# Variable to track total profit
profit = 0

# Function to check if there are enough ingredients to make the selected drink
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Function to process the coins inserted by the user
def process_coins():
    print("Please insert coins.")
    # Input number of each coin type and calculate total amount inserted
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

# Function to verify if the inserted money is sufficient
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# Function to prepare the coffee and deduct used ingredients
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

# Main loop to keep the machine running until user exits
machine_on = True
while machine_on:
    print_menu()
    choice = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
    
    if choice == "exit":
        machine_on = False
        print("Thank you for using the coffee machine!")
    
    elif choice == "report":
        # Display current resource levels and total earnings
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources.get('milk', 0)}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    
    elif choice in menu:
        drink = menu[choice]
        # Check resource availability
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            # Check if transaction was successful
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                profit += drink["cost"]  # Update profit
    else:
        print("Invalid selection. Please try again.")