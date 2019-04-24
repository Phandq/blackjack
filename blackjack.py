import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♣','♠','♦','❤']

# Create and return a shuffled deck with 52 cards
def createDeck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + " of " + suit)
    random.shuffle(deck)

    return deck

# Count value of cards in hand and return total value
def cardCount(hand):
    count = 0
    countAce = 0
    for i in hand:
        i = i.split()[0]
        if (i == 'J' or i == 'Q' or i == 'K'):
            count += 10
        elif (i != 'A'):
            count += int(i)
        else:
            countAce += 1
    
    # The value of ace can be either 1 or 11
    if(countAce == 1 and count <= 10):
        count += 11
    elif(countAce != 0):
        count += 1

    return count

# Dealer and player are dealt with two cards
def playingHands(deck):
    dealerHand = []
    playerHand = []
    hand = 0
    while(hand < 2):
        dealerHand.append(deck.pop())
        playerHand.append(deck.pop())
        hand += 1

    return [dealerHand, playerHand]

# Result from hit
def hit(dealer, dealerCount, player, playerHand):
    if(playerHand > 21):
        print("\nDealer has: \n" + str(dealer) + " for total of " + str(dealerCount))
        print("\nYou have: \n" + str(player) + " for total of " + str(playerHand))
        print("You busted, you lose.\n")
        playAgain()
    elif(playerHand == 21):
        print("\nDealer has: \n" + str(dealer) + " for total of " + str(dealerCount))
        print("\nYou have: \n" + str(player) + " for total of " + str(playerHand))
        print("You got a Blackjack!\n")
        playAgain()

# Result from stand
def stand(dealerHand, playerHand):
    if(playerHand == dealerHand):
        print("No one wins\n")
    elif(dealerHand == 21):
        print("You lose, Dealer got a Blackjack.\n")
    elif(dealerHand > 21):
        print("Dealer busted, you win!\n")
    elif(playerHand > dealerHand):
        print("You win!\n")
    elif(playerHand < dealerHand):
        print("You lose.\n")

def playAgain():
    restart = input("[P]lay again or [Q]uit? ")
    if(restart == 'p'):
        game()
    else:
        exit()

def game():
    print("-------------------------")
    print("| Welcome to Blackjack! |")
    print("-------------------------")  
    playerChoice = "p"
    deck = createDeck()
    hands = playingHands(deck)
    dealer = hands[0]
    player = hands[1]
    

    while(playerChoice != "q"):
        dealerCount = cardCount(dealer)
        playerCount = cardCount(player)
        print("\nDealer has: \n", dealer[0])
        print("\nYou have: \n" + str(player) + " for total of " + str(playerCount))
        playerChoice = input("\nDo you want to [H]it, [S]tand, or [Q]uit: ").lower()
        
        # Player "hit" (take a card)
        if(playerChoice == 'h'):
            player.append(deck.pop())
            playerCount = cardCount(player)
            hit(dealer, dealerCount, player, playerCount)
        # Player "stand" (end their turn)
        elif(playerChoice == 's'):
            # Dealer will hit until the cards total 17 or more points
            while dealerCount <= 16:
                dealer.append(deck.pop())
                dealerCount = cardCount(dealer)
            print("\nDealer has: \n", str(dealer) + "  for total of ", dealerCount)
            stand(dealerCount, playerCount)
            playAgain()
        elif(playerChoice == 'q'):
            print("\nThanks for playing!")
            exit()

# Initalize game
game()
