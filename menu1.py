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
                print("Delivery")
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
                print("Click and Collect")
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

    for count in range(len(drink_names)):
        print(drink_names[count], "$" + "{:.2f}".format(drink_prices[count]))

    # Rest of the code...

def main():
    welcome()
    delivery_or_click_collect()
    menu()

    # Rest of the code...

main()
