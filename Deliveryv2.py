import random

def greeting():
    names = ["Sakura", "Momo", "Hinata", "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    name = random.choice(names)

    print("*** Welcome to Drinks! ***")
    print(f"~ Konnichiwa! I'm {name}, your anime maid assistant ~")
    print("*** How may I assist you with your order today? ***")

def get_delivery_details():
    delivery_details = {}
    print("Sure! Let's start with the delivery details.")

    questions = [
        "May I have your name, please?",
        "What is your phone number?",
        "What will be your delivery address?",
        "Any specific delivery instructions?"
    ]

    for question in questions:
        answer = input(question + " ")
        delivery_details[question] = answer

    print("Thank you for providing the delivery details.")

    return delivery_details

def handle_delivery():
    print("Delivery")
    delivery_details = get_delivery_details()
    print("Great! Here are the delivery details:")
    for key, value in delivery_details.items():
        print(key.capitalize() + ":", value)

def get_click_collect_details():
    click_collect_details = {}
    print("Sure! Let's proceed with the click and collect details.")

    questions = [
        "May I have your name, please?",
        "What is your phone number?"
    ]

    for question in questions:
        answer = input(question + " ")
        click_collect_details[question] = answer

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
    greeting()
    delivery_or_click_collect()

    # Put the rest of code...

main()
