import random

dest = ["Paris", "New York", "Vancouver", "Cannon Beach"]
restaraunt = ["Chipotle", "Taco Bell", "Dominos", "24-Hour Diner"]
transport = ["plane", "train", "car", "bus"]
entertain = ["visiting museums", "bar-hopping", "hiking", "shopping"]

options = [dest, restaraunt, transport, entertain]

final_list = []

def get_random(list):
    random_item = random.choice(list)
    return random_item

def get_user_choice(list):
    user_choice = "n"
    while user_choice.lower() == "n":
            random_selection = get_random(list)
            user_choice = input(f"We have selected {random_selection} does this work for you? (Y/N): > ")
            if user_choice.lower() == "n":
                print("How about this?")
               
            else:
                print(f"Great! You have chosen {random_selection}.")
    final_list.append(random_selection)

def display_trip(list):
    print()
    print("Welcome to your Day-Trip Generator! Please select your options as they are displayed below!")
    print()

    for i, item in enumerate(list):
        get_user_choice(item)

    print(f'''
    Here is your finalized trip itinerary!

    Destination:  {final_list[0]}
    Restaurant:  {final_list[1]}
    Mode of Transportation:  {final_list[2]}
    Form of Entertainment:  {final_list[3]}
    ''')

display_trip(options)
    

