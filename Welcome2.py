import random

def welcome_greeting():
    maid_names = ["Sakura", "Momo", "Hinata", "Kotori", "Ayumi", "Natsuki", "Aoi", "Haru"]
    maid_name = random.choice(maid_names)

    print("*** Welcome to Drinks! ***")
    print(f"~ Hello! I'm {maid_name}, your friendly assistant ~")
    print("*** How may I assist you with your order today? ***")

welcome_greeting()

