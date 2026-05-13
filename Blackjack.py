import sys, random

# Set up the constants
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.

BACKSIDE = 'backside'

def main():
    print('''Blackjack
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens and Jacks are worth 10 points. 
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player. The dealer stops when he reaches 17.''')
    
    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Let the player enter their bet for this round:
        print(f'You have ${money}. What would you like to bet? ')
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print("Bet:", bet)
        while True: # Keep looping until player stands or busts
            displayHands(playerHand,dealerHand,False)
            print()

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D
            move = getMove(playerHand, money - bet)

            # Handle the player actions
            if move == 'D':
                # The player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H','D'):
                # Hit/Doubling down takes another card
                newCard = deck.pop()
                rank,suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted
                    continue
            if move in ('S','D'):
                # Stand/doubling down ends the player's turn
                break

        # Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
            # The dealer hits
                print('Dealer htis...')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # the dealer has busted
                input('Press Enter to continue....')
                print('\n\n')

        # Show the final hands
        displayHands(playerHand,dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost or tied
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
        elif (playerValue < dealerValue) or (playerValue > 21):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie! The bet is returned to you.')
        
        input('\nPress Enter to continue....')
        print('\n\n')

def getBet(maxBet):
    """ Ask the player how much they want to bet for this round."""
    while True: # Keep askingt till the player enters a valid amount
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()
        
        if not bet.isdecimal():
            continue #If the player didn't enter a number, ask again
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # If the player entered a valid amount, return it
        
def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, CLUBS, SPADES):
        for rank in range(2,11):
            deck.append((str(rank), suit)) # Add the numbered cards
        for rank in ('J','Q','K','A'):
            deck.append((rank, suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """SHow the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False"""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else: 
        print('DEALER: ???')
        # Hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
    
    # Show the player's cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value)"""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank) # Numbered cards are worth their number

    # Add the value for the aces:
    value += numberOfAces # Add 1 per ace
    for i in range(numberOfAces):
        # If another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10
    
    return value


def displayCards(cards):
    """Displays all the cards in the cards list"""
    rows = ['','','',''] # the text to display on each row
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Print the top line of the card
        if card == BACKSIDE:
            # Print a backside card
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            # Print the card's front
            rank, suit = card # The card is a tuple data structure
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2)) 
    # Print each row on the screen
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Asks the player for their move and returns 'H' or 'S'. 'H' means hit, 'D' means double down and 'S' means stay"""
    while True: # Keep asking until the player enters a correct move
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']
        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0: 
            moves.append('(D)ouble Down')

        # Get the player's move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        # Make sure the player enters a valid move
        if move in ('H','S'):
            return move # Player has entered a valid move 
        if move == 'D': # '(D)ouble down in moves:
            return move # Player has entered a valid move
        
if __name__ == '__main__':
    main() # Start the game