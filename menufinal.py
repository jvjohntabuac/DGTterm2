import random

def anime_maid_greeting():
    maid_names = ["Sakura", "Momo", "Hinata", "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    maid_name = random.choice(maid_names)

    print("*** Welcome to Drinks! ***")
    print(f"I'm {maid_name}, your anime maid assistant.")
    print("*** How may I assist you with your order today? ***")

def get_delivery_details():
    delivery_details = {}
    print("Please enter delivery information")
    delivery_details['name'] = input("Please enter your name: ")
    delivery_details['phone'] = input("Please enter your phone number: ")
    delivery_details['address'] = input("Address: ")
    delivery_details['instructions'] = input("Delivery instructions: ")
    return delivery_details

def handle_delivery():
    print("Delivery")
    delivery_details = get_delivery_details()
    print("Delivery details:")
    for key, value in delivery_details.items():
        print(key.capitalize() + ":", value)

def get_click_collect_details():
    click_collect_details = {}
    print("Sure! Let's proceed with the click and collect details.")

    click_collect_details['name'] = input("May I have your name, please? ")
    click_collect_details['phone'] = input("What is your phone number? ")

    store_options = ["Maid Café", "Anime Lounge", "Otaku Bar", "Sushi Shop"]
    print("Please choose a store for click and collect:")
    for i, store in enumerate(store_options, start=1):
        print(f"{i}. {store}")

    while True:
        try:
            store_choice = int(input("Enter the number of the store: "))
            if 1 <= store_choice <= len(store_options):
                selected_store = store_options[store_choice - 1]
                click_collect_details['store'] = selected_store
                print(f"You have chosen '{selected_store}' for click and collect.")
                break
            else:
                print("Invalid input. Please enter a valid store number.")
        except ValueError:
            print("Invalid input. Please enter a valid store number.")

    pickup_time = input("Please enter your preferred pickup time: ")
    click_collect_details['pickup_time'] = pickup_time

    order_number = random.randint(1000, 9999)
    click_collect_details["Order Number"] = order_number
    print("Randomly generated order number:", order_number)

    print("Thank you for providing the click and collect details.")

    return click_collect_details

def handle_click_collect():
    print("Click and Collect")
    click_collect_details = get_click_collect_details()
    print("Great! Here are the click and collect details:")
    for key, value in click_collect_details.items():
        print(key.capitalize() + ":", value)

def delivery_or_click_collect():
    while True:
        print("Press 1 for delivery or 2 for click and collect")
        try:
            user_choice = int(input("Please enter your choice (1 for Delivery, 2 for Click and Collect): "))
            if user_choice == 1:
                handle_delivery()
                return 'delivery'
            elif user_choice == 2:
                handle_click_collect()
                return 'click and collect'
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

def menu(delivery_option):
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
                print("Sorry, the maximum number of drinks allowed per order is 5. Please enter a valid number.")
            else:
                break
        else:
            print("That response is invalid. Please enter a number.")

    # Additional code to repeat the prompt when an invalid number is entered
    while num_drinks > 5:
        while True:
            num_drinks = input("Please enter a valid number of drinks (up to 5): ")
            if num_drinks.isdigit():
                num_drinks = int(num_drinks)
                if num_drinks <= 5:
                    break
            print("That is not acceptable. Please enter a number.")

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
        order_list.append((drink_names[drink_ordered], 1))  # Default quantity is set to 1

        while True:
            drink_quantity = input("Enter the quantity for {}: ".format(drink_names[drink_ordered]))
            if drink_quantity.isdigit() and 1 <= int(drink_quantity) <= 10:
                drink_quantity = int(drink_quantity)
                break
            else:
                print("Invalid quantity. Please enter a number between 1 and 10.")

        order_cost.append(drink_prices[drink_ordered] * drink_quantity)
        order_list[-1] = (drink_names[drink_ordered], drink_quantity)  # Update the quantity for the selected drink

        print("You have chosen {} (Quantity: {})".format(drink_names[drink_ordered], drink_quantity))

    total_price = sum(order_cost)

    # Apply discount for large orders
    if num_drinks > 3:
        discount = total_price * 0.1
        total_price -= discount
        print("Congratulations! Your order has been discounted by 10%.")

    print("Order list:")
    for drink_ordered, quantity in order_list:
        print(f"{quantity} {drink_ordered}")

    print("Total price: $", "{:.2f}".format(total_price))

    if delivery_option == 'delivery' and num_drinks >= 4: #fixed a problem that it prevents the user to choose delivery
        print("Congratulations! You qualify for free delivery!")

def main():
    anime_maid_greeting()
    delivery_option = delivery_or_click_collect()
    menu(delivery_option)

    # Rest of code...

main()
