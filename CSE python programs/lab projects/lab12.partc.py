
import cards

# Create the deck of cards
def create_deck():
    the_deck = cards.Deck()
    the_deck.shuffle()
    return the_deck
def starting_hands(the_deck):
    hands = []
    player1_hand = []
    player2_hand = []

    for x in range(2):
        card1 = the_deck.deal()
        player1_hand.append(card1)
        card2 = the_deck.deal()
        player2_hand.append(card2)

    print(player1_hand)
    print(player2_hand)
    hands.append(player1_hand)
    hands.append(player2_hand)
    return hands
def battle(deck, hand):
    starter = input("Do you want to battle? ")
    while True:
        starter = starter.lower()
        if starter == "no":
            break
        player1_hand = hand[0]
        player2_hand = hand[1]
        if player1_hand == []:
            return 2
        if player2_hand == []:
            return 1
        played1 = player1_hand.pop(0)
        print("Player 1 played: ", played1)
        played2 = player2_hand.pop(0)
        print("Player 2 played: ", played2)
        c1_value = played1.value()
        c2_value = played2.value()
        if c1_value == 1:
            c1_value = 500
        if c2_value == 1:
            c2_value = 500

        if  c1_value > c2_value:
            print("player 1 won")
            player1_hand.append(played1)
            player1_hand.append(played2)
            
        if c1_value < c2_value:
            print("player 2 won")
            player2_hand.append(played1)
            player2_hand.append(played2)

        if c1_value == c2_value:
            print("tie")
            player1_hand.append(played1)
            player2_hand.append(played2)

        print(player1_hand)
        print(player2_hand)
        starter = input("Do you want to battle? ")
    return 0

def main():
    deck = create_deck()
    hand = starting_hands(deck)
    
    x = battle(deck, hand)
    if x == 1:
        print("player 1 wins")
    elif x == 2:
        print("player 2 wins")
    else:
        if len(hand[0]) > len(hand[1]):
            print("player 1 wins")
        elif len(hand[0]) < len(hand[1]):
            print("player 2 wins")
        elif len(hand[0]) == len(hand[1]):
            print("tie game")
        else:
            print("error")
            

    print("game over")
main()
