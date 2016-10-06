from exercise_helper import pause, discuss, show

import cards
''' The basic process is this:
    1) You create a Deck instance, which is filled (automatically) with 52 Card instances
    2) You can deal those cards out of the deck into hands, each hand a list of cards
    3) You then manipulate cards as you add/remove them from a hand
'''

show(1)

my_deck = cards.Deck()
print("====== display my_deck before shuffling =====")
my_deck.display()

discuss()

show(2)

my_deck.shuffle()
print("====== display my_deck after shuffling it =====")
my_deck.display()

discuss()
pause(1)
# the deck class deals cards from the "top" of the deck
# the "top" of the deck is the end of the deck 
a_card = my_deck.deal()
print("Dealt card is:", a_card)
print('How many cards left:', len(my_deck))
print("Is the deck empty?", my_deck.is_empty())

discuss()
show(3)

print("===== my_deck now contains ====================")
my_deck.display()

pause(2)
# deal some hands and print
hand1_list=[]
hand2_list=[]
for i in range(5):
    c = my_deck.deal()
    hand1_list.append(c)
    c = my_deck.deal()
    hand2_list.append(c)
    
print("Hand 1:", hand1_list)
print("Hand 2:", hand2_list)
print("my_deck now contains:")
my_deck.display()

discuss()

pause(3)
# take the last card dealt out of each hand
last_card_hand1 = hand1_list.pop()
last_card_hand2 = hand2_list.pop()
print("last_card_hand1 is", last_card_hand1,
      ", last_card_hand2 is", last_card_hand2)
print("Hands are now:", hand1_list, hand2_list)

discuss()

pause(4)
# check the compares
if last_card_hand1.rank() == last_card_hand2.rank():
    print(last_card_hand1, last_card_hand2, "of equal rank")
elif last_card_hand1.rank() > last_card_hand2.rank():
    print(last_card_hand1, "of higher rank than", last_card_hand2)
else:
    print(last_card_hand2, "of higher rank than", last_card_hand1)

if last_card_hand1.value() == last_card_hand2.value():
    print(last_card_hand1, last_card_hand2, "of equal value")
elif last_card_hand1.value() > last_card_hand2.value():
    print(last_card_hand1, "of higher value than", last_card_hand2)
else:
    print(last_card_hand2, "of higher value than", last_card_hand1)

if last_card_hand1.suit() == last_card_hand2.suit():
    print(last_card_hand1,'of equal suit with', last_card_hand2)
else:
    print(last_card_hand1,'of different suit than', last_card_hand2)

discuss()
show(3)

print("===== my_deck now contains ====================")
my_deck.display()

pause(5)
# a foundation, a list of lists. 4 columns in this example
foundation_list = [[],[],[],[]]
column = 0
while not my_deck.is_empty():
    foundation_list[column%4].append(my_deck.deal())
    column += 1

for i in range(4):
    print("foundation",i,foundation_list[i])


