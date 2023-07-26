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
                print("Please enter delivery information")
                customer_details['name'] = input("Please enter your name: ")
                customer_details['phone'] = input("Please enter your phone number: ")
                customer_details['address'] = input("Address: ")
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
                print("Click and Collect details:")
                for key, value in customer_details.items():
                    print(key.capitalize() + ":", value)
                return customer_details, 'click and collect'
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

def menu(delivery_option):
    drink_names = ["Coca-Cola", "Pepsi", "Sprite", "Fanta", "Mountain Dew", "Dr. Pepper", "Iced Tea", "Lemonade", "Orange Juice", "Apple Juice", "Mango Smoothie", "Strawberry Shake", "Cappuccino", "Latte", "Espresso"]
    drink_prices = [1.50, 1.50, 1.50, 1.50, 1.75, 1.75, 1.25, 1.25, 2.00, 2.00, 3.50, 3.50, 2.50, 2.50, 2.50]

    for index, drink_name in enumerate(drink_names):
        print(f"{index+1}: {drink_name} - ${drink_prices[index]:.2f}")

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
        order_list.append((drink_names[drink_ordered], 1))

        while True:
            drink_quantity = input("Enter the quantity for {}: ".format(drink_names[drink_ordered]))
            if drink_quantity.isdigit() and 1 <= int(drink_quantity) <= 10:
                drink_quantity = int(drink_quantity)
                break
            else:
                print("Invalid quantity. Please enter a number between 1 and 10.")

        order_cost.append(drink_prices[drink_ordered] * drink_quantity)
        order_list[-1] = (drink_names[drink_ordered], drink_quantity)

        print("You have chosen {} (Quantity: {})".format(drink_names[drink_ordered], drink_quantity))

    total_price = sum(order_cost)

    if num_drinks > 3:
        discount = total_price * 0.1
        total_price -= discount
        print("Congratulations! Your order has been discounted by 10%.")

    if delivery_option == 'delivery' and num_drinks >= 4:
        print("Congratulations! You qualify for free delivery!")

    print("Order list:")
    for drink_ordered, quantity in order_list:
        print(f"{quantity} {drink_ordered}")

    print("Total price: $", "{:.2f}".format(total_price))

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

def main():
    welcome()
    customer_details, delivery_option = delivery_or_click_collect()
    order_list, total_price = menu(delivery_option)

    if confirm_order():
        print("\nOrder processing...")
#new function/s.......
        # Print customer details
        print("\n*** Customer Details ***")
        print("Delivery Option:", delivery_option.capitalize())
        print("Name:", customer_details['name'])
        print("Phone Number:", customer_details['phone'])
        if delivery_option == 'delivery':
            print("Address:", customer_details['address'])
            print("Delivery Instructions:", customer_details['instructions'])
        print("\n*** Order Summary ***")

        # Print order list and total price
        for drink_ordered, quantity in order_list:
            print(f"{quantity} {drink_ordered}")
        print("Total Price: $", "{:.2f}".format(total_price))
    else:
        print("\nThank you for visiting. Have a great day!")
#new transaction or exit here..........
#integar vaidation here...
#string checker here
main()

