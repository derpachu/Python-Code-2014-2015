def show(seg_num):

    SEGMENTS = [ \
        [\
            """my_deck = cards.Deck()""",
            """print("====== display my_deck before shuffling =====")""",
            """my_deck.display()"""
            ],
        [\
            """my_deck.shuffle()""",
            """print("====== display my_deck after shuffling it =====")""",
            """my_deck.display()"""
            ],
        [\
            """print("===== my_deck now contains ====================")""",
            """my_deck.display()"""
            ]
        ]

    print( "In show({}): ".format( seg_num ), end="" )
    print( "Press 'Enter' to see what the following code will print.")

    print(83*"-")
    for line in SEGMENTS[seg_num - 1]:
          print("| {:81s} |".format(line))
    print(83*"-")

    input()


        


def pause(seg_num):

    SEGMENTS = [ \
        [ \
            """# the deck class deals cards from the "top" of the deck""",
            """# the "top" of the deck is the end of the deck""",
            """a_card = my_deck.deal()""",
            """print("Dealt card is:", a_card)""",
            """print('How many cards left:', len(my_deck))""",
            """print("Is the deck empty?", my_deck.is_empty())"""
            ],
        [ \
            """hand1_list=[]""",
            """hand2_list=[]""",
            """for i in range(5):""",
            """    c = my_deck.deal()""",
            """    hand1_list.append(c)""",
            """    c = my_deck.deal()""",
            """    hand2_list.append(c)""",
            """""",
            """print("Hand 1:", hand1_list)""",
            """print("Hand 2:", hand2_list)""",
            """print("my_deck now contains:")""",
            """my_deck.display()"""
            ],
        [ \
            """last_card_hand1 = hand1_list.pop()""",
            """last_card_hand2 = hand2_list.pop()""",
            """print("last_card_hand1 is", last_card_hand1,""",
            """     ", last_card_hand2 is", last_card_hand2)""",
            """print("Hands are now:", hand1_list, hand2_list)"""
            ],
        [ \
            """if last_card_hand1.rank() == last_card_hand2.rank():""",
            """    print(last_card_hand1, last_card_hand2, "of equal rank")""",
            """elif last_card_hand1.get_rank() > last_card_hand2.get_rank():""",
            """    print(last_card_hand1, "of higher rank than", last_card_hand2)""",
            """else:""",
            """    print(last_card_hand2, "of higher rank than", last_card_hand1)""",
            """""",
            """if last_card_hand1.value() == last_card_hand2.value():""",
            """    print(last_card_hand1, last_card_hand2, "of equal value")""",
            """elif last_card_hand1.get_value() > last_card_hand2.get_value():""",
            """    print(last_card_hand1, "of higher value than", last_card_hand2)""",
            """else:""",
            """    print(last_card_hand2, "of higher value than", last_card_hand1)""",
            """""",
            """if last_card_hand1.suit() == last_card_hand2.suit():""",
            """    print(last_card_hand1,'of equal suit with', last_card_hand2)""",
            """else:""",
            """    print(last_card_hand1,'of different suit than', last_card_hand2)"""
            ],
        [ \
            """foundation_list = [[],[],[],[]]""",
            """column = 0""",
            """while not my_deck.is_empty():""",
            """    foundation_list[column%4].append(my_deck.deal())""",
            """    column += 1""",
            """    """,
            """for i in range(4):""",
            """    print("foundation",i,foundation_list[i])"""
            ]
        ]

    print("\nPause #{}.".format(seg_num), end=" ")
    print("What will be printed by the following code?")

    print(83*"-")
    for line in SEGMENTS[seg_num - 1]:
          print("| {:81s} |".format(line))
    print(83*"-")
          
    print("\nPress the 'Enter' key to continue.")
    input()
          
def check():
    print("\nCheck that your answer was correct.")
    print("Then press the 'Enter' key to continue.")
    input()

def discuss():
    print("\nPaused for discussion.  Press the 'Enter' key to continue.")
    input()
          
