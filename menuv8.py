import random  # Don't forget to import the 'random' module

def anime_maid_greeting():
    maid_names = ["Sakura", "Momo", "Hinata", "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    maid_name = random.choice(maid_names)

    print("*** Welcome to Drinks! ***")
    print(f"~ Konnichiwa! I'm {maid_name}, your anime maid assistant ~")
    print("*** How may I serve you today, master/mistress? ***")

def get_delivery_details():
    delivery_details = {}
    print("Please provide me with the necessary information for the delivery, senpai~")
    delivery_details['name'] = input("Please tell me your name, senpai: ")
    delivery_details['phone'] = input("What's your phone number, senpai? ")
    delivery_details['address'] = input("Please share your delivery address with me, senpai: ")
    delivery_details['instructions'] = input("Do you have any special delivery instructions, senpai? ")
    return delivery_details

def handle_delivery():
    print("Delivery")
    delivery_details = get_delivery_details()
    print("Thank you, senpai! Here are the delivery details:")
    for key, value in delivery_details.items():
        print(key.capitalize() + ":", value)

def get_click_collect_details():
    click_collect_details = {}
    print("Sure! Let's proceed with the click and collect details.")

    click_collect_details['name'] = input("May I have your name, please, senpai? ")
    click_collect_details['phone'] = input("What is your phone number, senpai? ")

    store_options = ["Maid Café", "Anime Lounge", "Otaku Bar", "Sushi Shop"]
    print("Please choose a store for click and collect, senpai:")
    for i, store in enumerate(store_options, start=1):
        print(f"{i}. {store}")

    while True:
        try:
            store_choice = int(input("Enter the number of the store, senpai: "))
            if 1 <= store_choice <= len(store_options):
                selected_store = store_options[store_choice - 1]
                click_collect_details['store'] = selected_store
                print(f"Understood, senpai! You have chosen '{selected_store}' for click and collect.")
                break
            else:
                print("Invalid input, senpai. Please enter a valid store number.")
        except ValueError:
            print("Invalid input, senpai. Please enter a valid store number.")

    pickup_time = input("Please enter your preferred pickup time, senpai: ")
    click_collect_details['pickup_time'] = pickup_time

    order_number = random.randint(1000, 9999)  # Corrected the random number generation
    click_collect_details["Order Number"] = order_number
    print("Randomly generated order number, senpai:", order_number)

    print("Thank you for providing the click and collect details, senpai~")

    return click_collect_details

def handle_click_collect():
    print("Click and Collect")
    click_collect_details = get_click_collect_details()
    print("Yay! Here are the click and collect details, senpai:")
    for key, value in click_collect_details.items():
        print(key.capitalize() + ":", value)

def delivery_or_click_collect():
    while True:
        print("Press 1 for delivery or 2 for click and collect, senpai~")
        try:
            user_choice = int(input("Please enter your choice (1 for Delivery, 2 for Click and Collect): "))
            if user_choice == 1:
                handle_delivery()
                return 'delivery'
            elif user_choice == 2:
                handle_click_collect()
                return 'click and collect'
            else:
                print("Sorry, senpai. I didn't catch that. Please enter 1 or 2.")
        except ValueError:
            print("Sorry, senpai. This is not a valid number.")
            print("Please enter 1 or 2.")

def main():
    anime_maid_greeting()
    delivery_option = delivery_or_click_collect()

    # Rest of the code...

main()

