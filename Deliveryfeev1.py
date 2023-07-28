import random

def anime_maid_greeting():
    maid_names = ["Sakura", "Momo", "Hinata",
                  "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    maid_name = random.choice(maid_names)

    print("*** Welcome to Anime Maid Café ***")
    print(f"~ Konnichiwa! I'm {maid_name}, your anime maid assistant ~")
    print("*** How may I assist you with your order today? ***")

def is_valid_phone_number(phone_number):
    return phone_number.startswith('+64') and phone_number[3:].isdigit() and len(phone_number[3:]) == 10

def delivery_or_click_collect():
    customer_details = {}

    print("Press 1 for delivery or 2 for click and collect")

    while True:
        try:
            choice = int(input("Please enter your choice (1 for Delivery, 2 for Click and Collect): "))
            if choice == 1:
                print("You have chosen delivery.")
                print("Please enter delivery information")
                customer_details['name'] = input("Please enter your name: ")
                customer_details['phone'] = input("Please enter your phone number: ")
                while not is_valid_phone_number(customer_details['phone']):
                    print("Invalid phone number. Phone number must start with '+64' and have 10 digits (excluding '+', '6', and '4').")
                    customer_details['phone'] = input("Please enter a valid phone number: ")

                customer_details['address'] = input("Delivery address: ")
                customer_details['instructions'] = input("Delivery instructions: ")
                print("Delivery details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                return customer_details, 'delivery'
            elif choice == 2:
                print("You have chosen click and collect.")
                print("Please enter click and collect information")
                customer_details['name'] = input("Please enter your name: ")
                customer_details['phone'] = input("Please enter your phone number: ")
                while not is_valid_phone_number(customer_details['phone']):
                    print("Invalid phone number. Phone number must start with '+64' and have 10 digits (excluding '+', '6', and '4').")
                    customer_details['phone'] = input("Please enter a valid phone number: ")

                print("Click and Collect details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                return customer_details, 'click and collect'
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

def apply_delivery_fee(delivery_option, num_drinks, total_price):
    delivery_fee = 9.0
    if delivery_option == 'delivery' and num_drinks >= 4:
        print("Congratulations! You qualify for free delivery!")
        delivery_fee = 0.0

    total_price += delivery_fee
    return total_price

def menu(delivery_option):
    drink_names = ["Coca-Cola", "Pepsi", "Sprite", "Fanta", "Mountain Dew", "Dr. Pepper", "Iced Tea", "Lemonade",
                   "Orange Juice", "Apple Juice", "Mango Smoothie", "Strawberry Shake", "Cappuccino", "Latte", "Espresso"]
    drink_prices = [1.50, 1.50, 1.50, 1.50, 1.75, 1.75,
                    1.25, 1.25, 2.00, 2.00, 3.50, 3.50, 2.50, 2.50, 2.50]

    for index, drink_name in enumerate(drink_names):
        print(f"{index+1}: {drink_name} - ${drink_prices[index]:.2f}")

    order_list = []
    total_price = 0.0

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

    while num_drinks > 5:
        while True:
            num_drinks = input("Please enter a valid number of drinks (up to 5): ")
            if num_drinks.isdigit():
                num_drinks = int(num_drinks)
                if num_drinks <= 5:
                    break
            print("Invalid input. Please enter a number.")

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

        drink_price = drink_prices[drink_ordered] * drink_quantity
        order_list.append((drink_names[drink_ordered], drink_quantity))
        total_price += drink_price

        print("You have chosen {} (Quantity: {})".format(drink_names[drink_ordered], drink_quantity))

    total_price = apply_delivery_fee(delivery_option, num_drinks, total_price)

    print("Order list:")
    for drink_ordered, quantity in order_list:
        print(f"{quantity} {drink_ordered}")

    print("Total price (excluding delivery fee): ${:.2f}".format(total_price - 9.0))
    print("Delivery fee: $9.00")
    print("Total price (including delivery fee): ${:.2f}".format(total_price))
    return order_list, total_price

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

def new_transaction():
    while True:
        choice = input("Would you like to place a new order? (Y/N): ")
        if choice.lower() == 'y':
            order_list.clear()
            return True
        elif choice.lower() == 'n':
            print("Your order has been canceled.")
            return False
        else:
            print("Invalid input. Please enter Y or N.")

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

order_list = []

def main():
    while True:
        anime_maid_greeting()
        customer_details, delivery_option = delivery_or_click_collect()
        order_list, total_price = menu(delivery_option)

        if order_list is not None:
            if confirm_order():
                print("\nOrder processing...")

                # Additional code for order processing goes here

                print("\n*** Customer Details ***")
                print("Delivery Option:", delivery_option.capitalize())
                print("Name:", customer_details['name'])
                print("Phone Number:", customer_details['phone'])
                if delivery_option == 'delivery':
                    print("Address:", customer_details['address'])
                    print("Delivery Instructions:", customer_details['instructions'])
                print("\n*** Order Summary ***")

                # ... (existing code remains the same)
                # ... existing code=time of collect from click and collect v4-v5
                # ... existing code=order Number and put print order number from click and collect version 4-5 if needed else=none
                # .... other order or exit
                # ...delivery fee 9$ if delivery is not free, print it on the customer details

            if not ask_exit_or_new_order():
                break
            else:
                print("\nStarting a new order...")

        else:
            print("No items selected. Order canceled.")


main()


