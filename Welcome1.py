import random

def welcome_ver1():
    names = ["John", "Michel", "Ana", "Hizhenberg", "Luke", "Jonathan", "Michel", "Alex", "Iris", "Mia"]
    name = random.choice(names)
    print("*** Welcome to Drinks ***")
    print("My name is", name)
    print("*** I will be here to help with your order ***")

welcome_ver1()
#ver1 of the welcome code and it chooses a name succesfuly 
#i'd say it's fuctionable however it's rather too simple and bland to pass my expectation