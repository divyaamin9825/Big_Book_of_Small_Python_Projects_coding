"""
Birthday Paradox Simulation. 
This script simulates the birthday paradox, which states that in a group of x people, 
there is a probability greater than 50% that two people share the same birthday. 
"""
import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays.
    """
    birthdays = []
    for i in range(numberOfBirthdays):
        # the year is unimportant for this sim, as long as all birthdays have the same year
        startOfYear = datetime.date(2001,1,1)

        # get a random day of the year into the birthday list
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so there is no match.
    
    #compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA # return the matching birthday
            
# Display the intro:
print('''Birthday Paradox Simulation.
      The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
      The program uses a Monte Carlo simulation to explore this concept.''')

# Set up a tuple of month names in order
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount
    print('Invalid input. Please enter a number between 1 and 100.')
print()

# Generate and display the birthdays:
print('Here are {} birthdays:'.format(numBDays))
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText,end='')
print()
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Multiple people have the same birthday: {}'.format(dateText))
else:
    print('No one has the same birthday.')

print()
# Run through 100000 simulations
print('Generating', numBDays, 'random birthdays...')
input('Press Enter to begin.....')

print('Let\'s run another 100000 simulations to see how often we get two matching birthdays.')
simMatch = 0 # how many sims had matching birthdays in them
for i in range(100000):
    # Report on the progress every 100000 simulations
    if (i % 10000 == 0):
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print('100000 simulations run.')

# Display results
probablity = round(simMatch / 100000 * 100,2)
print('Out of 100000 simulations of', numBDays, 'people, there was a matching birthday in that group', simMatch, 'times. This means that')
print(numBDays, 'people have a', probablity, '% chance of having a matching birthday in their group')
