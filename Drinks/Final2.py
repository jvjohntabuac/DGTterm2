# Import the random module to generate random choices
import random

# Function to get non-empty input from the user
def get_non_empty_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value.strip()
        else:
            print("This field cannot be left blank. Please try again.")

# Greeting with a randomly chosen name from the list
def anime_maid_greeting():
    # List of names
    maid_names = ["Sakura", "Momo", "Hinata", "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    # Randomly select a name from the list
    maid_name = random.choice(maid_names)

    # Display the maid greeting with the chosen name
    print("*** Welcome to Anime Maid Café ***")
    print(f"~ Konnichiwa! I'm {maid_name}, your anime maid assistant ~")
    print("*** How may I assist you with your order today? ***")

# Check if the given phone number is valid (starts with '+64' and has 10 digits)
def is_valid_phone_number(phone_number):
    return phone_number.startswith('+64') and phone_number[3:].isdigit() and len(phone_number[3:]) == 10

# The customer to choose delivery or click and collect
def delivery_or_click_collect():
    customer_details = {}

    print("Press 1 for delivery or 2 for click and collect")

    while True:
        try:
            # Get the customer's choice
            choice = int(input("Please enter your choice (1 for Delivery, 2 for Click and Collect): "))
            if choice == 1:
                # Customer chooses delivery
                print("You have chosen delivery.")
                print("Please enter delivery information")
                # Get customer details for delivery
                customer_details['name'] = get_non_empty_input("Please enter your name: ")
                customer_details['phone'] = get_non_empty_input("Please enter your phone number: ")
                # Validate the phone number for delivery
                while not is_valid_phone_number(customer_details['phone']):
                    print("Invalid phone number. Phone number must start with '+64' and have 10 digits (excluding '+', '6', and '4').")
                    customer_details['phone'] = get_non_empty_input("Please enter a valid phone number: ")

                customer_details['address'] = get_non_empty_input("Delivery address: ")
                customer_details['instructions'] = input("Delivery instructions: ")
                print("Delivery details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                return customer_details, 'delivery'
            elif choice == 2:
                # Customer chooses click and collect
                print("You have chosen click and collect.")
                print("Please enter click and collect information")
                # Get customer details for click and collect
                customer_details['name'] = get_non_empty_input("Please enter your name: ")
                customer_details['phone'] = get_non_empty_input("Please enter your phone number: ")
                # Validate the phone number for click and collect
                while not is_valid_phone_number(customer_details['phone']):
                    print("Invalid phone number. Phone number must start with '+64' and have 10 digits (excluding '+', '6', and '4').")
                    customer_details['phone'] = get_non_empty_input("Please enter a valid phone number: ")

                print("Click and Collect details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                return customer_details, 'click and collect'
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

# Apply the delivery fee if applicable
def apply_delivery_fee(delivery_option, num_drinks, total_price):
    delivery_fee = 9.0
    # If the delivery option is chosen and the number of drinks is 4 or more, offer free delivery
    if delivery_option == 'delivery' and num_drinks >= 4:
        print("Congratulations! You qualify for free delivery!")
        delivery_fee = 0.0

    # Add the delivery fee to the total price
    total_price += delivery_fee
    return total_price

# Display the menu, take customer's order, and calculate the total price
def menu(delivery_option):
    # List of drink names and their corresponding prices
    drink_names = ["Coca-Cola", "Pepsi", "Sprite", "Fanta", "Mountain Dew", "Dr. Pepper", "Iced Tea", "Lemonade", "Orange Juice", "Apple Juice", "Mango Smoothie", "Strawberry Shake", "Cappuccino", "Latte", "Espresso"]
    drink_prices = [1.50, 1.50, 1.50, 1.50, 1.75, 1.75, 1.25, 1.25, 2.00, 2.00, 3.50, 3.50, 2.50, 2.50, 2.50]

    # Display the menu to the customer
    for index, drink_name in enumerate(drink_names):
        print(f"{index+1}: {drink_name} - ${drink_prices[index]:.2f}")

    order_list = []
    total_price = 0.0

    # Ask the customer how many drinks they want to order (up to 5)
    while True:
        num_drinks = input("How many drinks do you want? ")
        if num_drinks.isdigit():
            num_drinks = int(num_drinks)
            if num_drinks > 5:
                print("Sorry, the maximum number of drinks allowed per order is 5. Please enter a valid number.")
            else:
                break
        else:
            print("Invalid input. Please enter a number.")

    # Loop until the customer enters a valid number of drinks (up to 5)
    while num_drinks > 5:
        while True:
            num_drinks = input("Please enter a valid number of drinks (up to 5): ")
            if num_drinks.isdigit():
                num_drinks = int(num_drinks)
                if num_drinks <= 5:
                    break
            print("Invalid input. Please enter a number.")

    # Take the customer's drink order
    for _ in range(num_drinks):
        while True:
            drink_ordered = input("Choose the drink (enter the number): ")
            if drink_ordered.isdigit() and 0 < int(drink_ordered) <= len(drink_names):
                drink_ordered = int(drink_ordered) - 1
                break
            else:
                print("Invalid drink choice. Please try again.")

        while True:
            drink_quantity = input("Enter the quantity for {}: ".format(drink_names[drink_ordered]))
            if drink_quantity.isdigit() and 1 <= int(drink_quantity) <= 10:
                drink_quantity = int(drink_quantity)
                break
            else:
                print("Invalid quantity. Please enter a number between 1 and 10.")

        # Calculate the price for the chosen drink and quantity and add it to the order list and total price
        drink_price = drink_prices[drink_ordered] * drink_quantity
        order_list.append((drink_names[drink_ordered], drink_quantity))
        total_price += drink_price

        print("You have chosen {} (Quantity: {})".format(drink_names[drink_ordered], drink_quantity))

    # Apply the delivery fee if applicable
    total_price = apply_delivery_fee(delivery_option, num_drinks, total_price)

    # Display the order list and total price to the customer
    print("Order list:")
    for drink_ordered, quantity in order_list:
        print(f"{quantity} {drink_ordered}")

    print("Total price (excluding delivery fee): ${:.2f}".format(total_price - 9.0))
    print("Delivery fee: $9.00")
    print("Total price (including delivery fee): ${:.2f}".format(total_price))
    return order_list, total_price

# Ask the customer to confirm their order
def confirm_order():
    while True:
        choice = input("Would you like to confirm your order? (Y/N): ")
        if choice.lower() == 'y':
            print("Thank you! Your order has been confirmed.")
            return True
        elif choice.lower() == 'n':
            print("Your order has been canceled.")
            return False
        else:
            print("Invalid input. Please enter Y or N.")

# Ask the customer if they want to place a new order
def new_transaction():
    while True:
        choice = input("Would you like to place a new order? (Y/N): ")
        if choice.lower() == 'y':
            # Clear the order_list to start a new order
            order_list.clear()
            return True
        elif choice.lower() == 'n':
            print("Your order has been canceled.")
            return False
        else:
            print("Invalid input. Please enter Y or N.")

# Ask the customer if they want to create a new order or exit
def ask_exit_or_new_order():
    while True:
        choice = input("Would you like to create a new order (N) or exit (E)? ").lower()
        if choice == 'n':
            return True
        elif choice == 'e':
            print("Thank you for visiting Anime Maid Café. Have a great day!")
            return False
        else:
            print("Invalid input. Please enter 'N' to create a new order or 'E' to exit.")

# List to store the customer's order
order_list = []

# Main function to handle the order process
def main():
    while True:
        # Greet the customer with a random maid name
        anime_maid_greeting()
        # Get delivery/click and collect information from the customer
        customer_details, delivery_option = delivery_or_click_collect()
        # Display the menu, take the order, and calculate the total price
        order_list, total_price = menu(delivery_option)

        # Check if there are any items in the order list (i.e., the customer placed an order)
        if order_list:
            # Confirm the order with the customer
            if confirm_order():
                print("\nOrder processing...")

            # Check if the customer wants to create a new order or exit the program
            if not ask_exit_or_new_order():
                break
            else:
                print("\nStarting a new order...")

        else:
            print("No items selected. Order canceled.")

# Start the order process by calling the main function
main()



