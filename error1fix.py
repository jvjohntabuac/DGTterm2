from random import choice, randint

def welcome():
    names = ["John", "Michel", "Ana", "Heisenberg", "Luke", "Jonathan", "Michel", "Alex", "Iris", "Mia"]
    name = choice(names) 
    print("*** Welcome to Drinks ***")
    print("My name is", name)
    print("*** I will be here to help with your order ***")

def delivery():
    customer_details = {}

    print("Please enter delivery information")


def main():
    welcome()
    print("Press 1 for delivery or 2 for click and collect")
    

main()
#how i fix it adds the line 'name = choice(names)' this makes the part where the bot chooses a name from the list