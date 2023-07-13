from random import choice

def welcome():
    names = ["John", "Michel", "Ana", "Hizhenberg", "Luke", "Jonathan", "Michel", "Alex", "Iris", "Mia"]
    name = choice(names)
    print("*** Welcome to Drinks ***")
    print("My name is", name)
    print("*** I will be here to help with your order ***")

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
    print("Please enter click and collect information")
    click_collect_details['name'] = input("Please enter your name: ")
    click_collect_details['phone'] = input("Please enter your phone number: ")
    return click_collect_details

def handle_click_collect():
    print("Click and Collect")
    click_collect_details = get_click_collect_details()
    print("Click and Collect details:")
    for key, value in click_collect_details.items():
        print(key.capitalize() + ":", value)

def delivery_or_click_collect():
    while True:
        print("Press 1 for delivery or 2 for click and collect")
        try:
            user_choice = int(input("Please enter your choice (1 for Delivery, 2 for Click and Collect): "))
            if user_choice == 1:
                handle_delivery()
                break
            elif user_choice == 2:
                handle_click_collect()
                break
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

def main():
    welcome()
    delivery_or_click_collect()

    # Rest of the code...

main()
