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

destinations = []
restaurants = []
modes_of_transport = []
forms_of_entertainment = []
options = [destinations, restaurants, modes_of_transport, forms_of_entertainment]

random_dest = random.choice(destinations)
ramdom_restaurant = random.choice(restaurants)
random_mode_of_transport = random.choice(modes_of_transport)
random_form_of_entertainment = random.choice(forms_of_entertainment)

random_trip = input(f"You will spend the day at {random_dest} doing {random_form_of_entertainment}. You will get there via {random_mode_of_transport} and eat at {ramdom_restaurant}. Is this a trip you would like to take? (Y/N) > ")

def do_you_like_trip_options():
    while True:
        if random_trip == "y".lower():
            print("Great, have fun!")
            break
        elif random_trip == "n".lower():
            what_changes_would_you_like_to_make()
        else:
            print("Please type 'Y' or 'N'.")

def what_changes_would_you_like_to_make(): 
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    change_to_make = input("Which element of your trip would you like to change? (enter number corresponding with item you would like to change) > ")

    if change_to_make == 1:
        random_dest
        print(random_trip)
        do_you_like_trip_options()
    elif change_to_make == 2:
        ramdom_restaurant
        print(random_trip)
    elif change_to_make == 3:
        random_mode_of_transport
        print(random_trip)
    elif change_to_make == 4:
        random_form_of_entertainment
        print(random_trip)
    else:
        print("Sorry, it looks like that wasn't an option. Please type the number corresponding with the item you would like to change.")

def more_changes():
    more_changes = input("Would you like to make any other changes to your day trip (Y/N) > ")

    while True:
        if more_changes == "y".lower():
            what_changes_would_you_like_to_make()
        elif more_changes == "n".lower():
            print("Great! Enjouy your trip!")
            break
        else:
            print("Please type 'Y' or 'N'.")

