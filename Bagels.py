"""
Bagels, a deductive logic game.
The game consists of three-digit numbers where the first digit is not zero.
The player tries to guess the number, and after each guess, they receive clues:
- "Pico" for each correct digit in the wrong position.
- "Fermi" for each correct digit in the correct position.
- "Bagels" if no digit is correct.
The player keeps guessing until they find the correct number.
"""

import random
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''BAGELS, a deductive logic game.
          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say:               That means:
          Pico                      One digit is correct and in the wrong position.
          Fermi                     One digit is correct and in the correct position.
          Bagels                    No digit is correct.
    For example, if the secret number was 248 and you guess was 843, the clues would be Fermi Pico'''.format(NUM_DIGITS))

    while True: # main game loop
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1 # number of guesses the player has made
        while numGuesses <= MAX_GUESSES:
            guess = '' 
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # they're correct so we break out of this loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses. The answer was {}.'.format(secretNum))
            
            # Ask player if they want to play again
            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
            print('Thanks for playing!')



def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # create a list of digits 0-9
    random.shuffle(numbers) # shuffle the list in random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the wrong place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all.
    else:
        # sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of clues.
        return ' '.join(clues)
    
# If the program is run (instead of imported as a module), run the game:    
if __name__ == '__main__':
    main()