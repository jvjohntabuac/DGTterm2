import random

def anime_maid_greeting():
    maid_names = ["Sakura", "Momo", "Hinata", "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    maid_name = random.choice(maid_names)

    print("*** Welcome to Drinks! ***")
    print(f"~ Konnichiwa! I'm {maid_name}, your anime maid assistant ~")
    print("*** How may I assist you with your order today? ***")

def get_delivery_details():
    delivery_details = {}
    print("Please enter delivery information")
    delivery_details['name'] = input("Please enter your name: ")
    delivery_details['phone'] = input("Please enter your phone number: ")
    delivery_details['address'] = input("Address: ")
    delivery_details['instructions'] = input("Delivery instructions: ")
    return delivery_details

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

def handle_delivery():
    print("Delivery")
    delivery_details = get_delivery_details()
    print("Delivery details:")
    for key, value in delivery_details.items():
        print(key.capitalize() + ":", value)

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
                return "delivery"
            elif user_choice == 2:
                handle_click_collect()
                return "click and collect"
            else:
                print("Wrong input, please enter 1 or 2.")
        except ValueError:
            print("This is not a valid number.")
            print("Please enter 1 or 2.")

def main():
    anime_maid_greeting()
    delivery_option = delivery_or_click_collect()

    # Rest of the code...

main()



