'''
(5 points): As a developer, I want to make at least three commits with descriptive messages 
(5 points):  As a developer, I want to store my destinations, restaurants, 
mode of transportation, and entertainment in their own separate Lists. 
(5 points): As a user, I want a destination to be randomly selected for my day trip. 
(5 points): As a user, I want a restaurant to be randomly selected for my day trip
(5 points): As a user, I want a mode of transportation to be randomly selected for 
my day trip. 
(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
(15 points): As a user, I want to be able to randomly re-select a destination, 
restaurant, mode of transportation, and/or form of entertainment if I dont like one or 
more of those things.
(10 points): As a user, I want to be able to confirm that my day trip is “complete” 
once I like all of the random selections.
(10  points): As a user, I want to display my completed trip in the console
(5 points): Single Responsibility: As a developer, I want all of my functions to have a 
Single Responsibility. Remember, each function should do just one thing! 
'''

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


# def display_potential_trip(option_type, list__of_options):
#     for option in list__of_options:
#         if option_type == destinations:
#             final_trip.append(get_random(destinations))
#         elif option_type == restaurants:
#             final_trip.append(get_random(restaurants))
#         elif option_type == modes_of_transport:
#             final_trip.append(get_random(modes_of_transport))
#         elif option_type == forms_of_entertainment:
#             final_trip.append(get_random(forms_of_entertainment))

#display options(optoin_index, options)
#for option in options(options_index)
    # for option in options:
    #     get_random(option)
    #     final_trip.append(option)


# def do_you_like_trip_options():
#     are_you_happy = input("Are you satisfied with your trip? (Y/N) > ")
#     while True:
#         if are_you_happy == "y".lower():
#             print("Great, have fun!")
#             break
#         elif are_you_happy == "n".lower():
#             what_changes_would_you_like_to_make()
#         else:
#             print("Please type 'Y' or 'N'.")

# def what_changes_would_you_like_to_make(): 
#     print("Parts of your trip you can edit:")
#     print()
#     for i, option in enumerate(options):
#         print(f"{i + 1}. {option}")
#     print()
#     change_to_make = int(input("Which element of your trip would you like to change? (enter number corresponding with item you would like to change) > "))

#     while True:

#         if change_to_make.isnumeric() == True:
#             if change_to_make == 1:
#                 new_dest = get_random(destinations)
#                 final_trip[0] = new_dest
#                 are_you_happy_II()
#             elif change_to_make == 2:
#                 new_rest = get_random(restaurants)
#                 final_trip[1] = new_rest
#                 are_you_happy_II()
#             elif change_to_make == 3:
#                 new_trans = get_random(modes_of_transport)
#                 final_trip[2] = new_trans
#                 are_you_happy_II()
#             elif change_to_make == 4:
#                 new_ent = get_random(forms_of_entertainment)
#                 final_trip[3] = new_ent
#                 are_you_happy_II()
#         else:
#             print("Sorry, it looks like that wasn't an option. Please type the number corresponding with the item you would like to change.")

# def are_you_happy_II():
#     more_changes = input("Would you like to make any other changes to your day trip (Y/N) > ")

#     while True:
#         if more_changes == "y".lower():
#             what_changes_would_you_like_to_make()
#         elif more_changes == "n".lower():
#             print("Great! Enjouy your trip!")
#             break
#         else:
#             print("Please type 'Y' or 'N'.")

# def run_program(list):
#     for item in list:
#         display_potential_trip(item, list)

# run_program(options)

#also had issues setting up the run-program function - things fell apart quickly here 


# def run_day_trip_program():

#     print("Welcome to your interactive day trip generator! Below is one option for your trip!")
#     print()

#     satisfied = False

#     while satisfied == False:

#         display_potential_trip(options)
#         print()

# run_day_trip_program()

# random_dest = random.choice(destinations)
# random_restaurant = random.choice(restaurants)
# random_mode_of_transport = random.choice(modes_of_transport)
# random_form_of_entertainment = random.choice(forms_of_entertainment)

# trip_dest = get_random(destinations)
# final_trip.append(trip_dest)
# trip_rest = get_random(restaurants)
# final_trip.append(trip_rest)
# trip_transport = get_random(modes_of_transport)
# final_trip.append(trip_transport)
# trip_entertainment = get_random(forms_of_entertainment)
# final_trip.append(trip_entertainment)