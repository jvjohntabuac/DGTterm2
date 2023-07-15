from random import choice

def welcome():
    names = ["John", "Michel", "Ana", "Hizhenberg", "Luke", "Jonathan", "Michel", "Alex", "Iris", "Mia"]
    name = choice(names)
    print("*** Welcome to Drinks ***")
    print("My name is", name)
    print("*** I will be here to help with your order ***")

def delivery_or_click_collect():
    customer_details = {}

    print("Press 1 for delivery or 2 for click and collect")
    
    while True:
        try:
            choice = int(input("Please enter your choice (1 for Delivery, 2 for Click and Collect): "))
            if choice == 1:
                print("You have chosen delivery.")
                # Ask for additional delivery details
                print("Please enter delivery information")
                customer_details['name'] = input("Please enter your name: ")
                customer_details['phone'] = input("Please enter your phone number: ")
                customer_details['address'] = input("Address: ")
                customer_details['instructions'] = input("Delivery instructions: ")

                # Print delivery details
                print("Delivery details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                break
            elif choice == 2:
                print("You have chosen click and collect.")
                # Ask for click and collect details
                print("Please enter click and collect information")
                customer_details['name'] = input("Please enter your name: ")
                customer_details['phone'] = input("Please enter your phone number: ")

                # Print click and collect details
                print("Click and Collect details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                break
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

def menu():
    # Drinks menu
    drink_names = ["Coca-Cola", "Pepsi", "Sprite", "Fanta", "Mountain Dew", "Dr. Pepper", "Iced Tea", "Lemonade", "Orange Juice", "Apple Juice", "Mango Smoothie", "Strawberry Shake", "Cappuccino", "Latte", "Espresso"]
    drink_prices = [1.50, 1.50, 1.50, 1.50, 1.75, 1.75, 1.25, 1.25, 2.00, 2.00, 3.50, 3.50, 2.50, 2.50, 2.50]

    for index, drink_name in enumerate(drink_names):
        print(f"{index+1}: {drink_name} - ${drink_prices[index]:.2f}")

    # Ask for the number of drinks
    while True:
        num_drinks = input("How many drinks do you want? ")
        if num_drinks.isdigit():
            num_drinks = int(num_drinks)
            if num_drinks > 5:
                print("Sorry, the maximum number of drinks allowed is 5. Please enter a valid number.")
            else:
                break
        else:
            print("Invalid input. Please enter a number.")

    # Additional code to repeat the prompt when an invalid number is entered
    while num_drinks > 5:
        while True:
            num_drinks = input("Please enter a valid number of drinks (up to 5): ")
            if num_drinks.isdigit():
                num_drinks = int(num_drinks)
                if num_drinks <= 5:
                    break
            print("Invalid input. Please enter a number.")

    order_list = []
    order_cost = []

    for _ in range(num_drinks):
        while True:
            drink_ordered = input("Choose the drink (enter the number): ")
            if drink_ordered.isdigit() and 0 < int(drink_ordered) <= len(drink_names):
                drink_ordered = int(drink_ordered) - 1
                break
            else:
                print("Invalid drink choice. Please try again.")
        order_list.append(drink_names[drink_ordered])
        order_cost.append(drink_prices[drink_ordered])

    total_price = sum(order_cost)

    if num_drinks >= 4:
        print("Congratulations! You qualify for free delivery!")

    print("Order list:")
    for drink_ordered in order_list:
        print(drink_ordered)

    print("Total price: $", "{:.2f}".format(total_price))

def main():
    welcome()
    delivery_or_click_collect()
    menu()

    # Rest of the code...

main()

