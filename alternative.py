import random

entertainment = ['Concert', 'Hiking', 'Horse back', 'Fishing', 'Sky Diving']
destination = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California']
transportation = ['Car', 'Bike', 'Roller Skates', 'Truck', 'Plane']
dinning = ['Spanish', 'Southern', 'Indian', 'Chinese', 'Italian']

vacation = []

for catergory in [entertainment, destination, transportation, dinning]:
    
    is_happy = 'n'
    
    while is_happy != 'y':
        
        index = random.randint(0, len(catergory)-1)
        choice = (catergory[index])
        
        is_happy = input(f'Your choice is {choice} are you happy with that? (y/n): ').lower()
    vacation.append(choice)

print(f'Your entertainment is {vacation[0]}, in {vacation[1]}, you will get there by {vacation[2]} you will eat {vacation[3]} food.')