#create a game of basic solitare
#DO NOT GO OVER 79 CHARACTERS
#use all the nessessary funcitons and their respective inputs
#DOC STRINGS DO THEM

import cards #gets the nessessary data

def initial_deal(deck):
    """creates the main format and fills up the cards
input: the deck to be distributed
output: dictionary of lists of all important categories"""
    main_game = {}#creates the main parts of the game
    f1 = [0]
    f2 = [0]
    f3 = [0]
    f4 = [0]
    stock = []
    waste = []
    tab1 = []
    tab2 = []
    tab3 = []
    tab4 = []
    tab5 = []
    tab6 = []
    tab7 = []

    delt_card = deck.deal()#deals out the cards to go into the tableau
    if delt_card.rank() != 10:
        delt_card = delt_card
    tab1.append(delt_card)
    tab1.insert(0, len(tab1))
    counter = tab1[0]
    for i in range(13-counter):
        tab1.append("  ")
        
    i = 0#repeated for all 7 stacks and deals into the list of cards
    for i in range(2):
        delt_card = deck.deal()
        if delt_card.rank() != 10:
            delt_card = delt_card
        tab2.append(delt_card)
    tab2.insert(0, len(tab2))
    counter = tab2[0]
    for i in range(13-counter):
        tab2.append("  ")
        
    i = 0
    for i in range(3):#reapeated
        delt_card = deck.deal()
        if delt_card.rank() != 10:
            delt_card = delt_card
        tab3.append(delt_card)
    tab3.insert(0, len(tab3))
    counter = tab3[0]
    for i in range(13-counter):
        tab3.append("  ")
        
    i = 0
    for i in range(4):#repeated
        delt_card = deck.deal()
        if delt_card.rank() != 10:
            delt_card = delt_card
        tab4.append(delt_card)
    tab4.insert(0, len(tab4))
    counter = tab4[0]
    for i in range(13-counter):
        tab4.append("  ")
        
    i = 0
    for i in range(5):#repeated
        delt_card = deck.deal()
        if delt_card.rank() != 10:
            delt_card = delt_card
        tab5.append(delt_card)
    tab5.insert(0, len(tab5))
    counter = tab5[0]
    for i in range(13-counter):
        tab5.append("  ")
        
    i = 0
    for i in range(6):#repeated
        delt_card = deck.deal()
        if delt_card.rank() != 10:
            delt_card = delt_card
        tab6.append(delt_card)
    tab6.insert(0, len(tab6))
    counter = tab6[0]
    for i in range(13-counter):
        tab6.append("  ")
        
    i = 0
    for i in range(7):#repeated
        delt_card = deck.deal()
        if delt_card.rank() != 10:
            delt_card = delt_card
        tab7.append(delt_card)
    tab7.insert(0, len(tab7))
    counter = tab7[0]
    for i in range(13-counter):
        tab7.append("  ")

    waste = [deck.deal()]#deals one card into the starting waste

    while not deck.is_empty():#deals the rest into the sotck
        stock.append(deck.deal())
    
    main_game["f1"] = f1 #just formats everything to be properly outputed
    main_game["f2"] = f2
    main_game["f3"] = f3
    main_game["f4"] = f4
    main_game["stock"] = stock
    main_game["waste"] = waste
    main_game["tab1"] = tab1
    main_game["tab2"] = tab2
    main_game["tab3"] = tab3
    main_game["tab4"] = tab4
    main_game["tab5"] = tab5
    main_game["tab6"] = tab6
    main_game["tab7"] = tab7
    
    template1 = """stock waste             foundation"""#creates the base shape of the game
    template2 = """{}    {}                {},{},{},{}"""
    template3 = """       tableau"""
    template5 = """{} | {} | {} | {} | {} | {} | {}"""
    
    print(template1)
    print(template2.format(main_game["stock"][0], main_game["waste"][0], \
                           main_game["f1"][0], main_game["f2"][0], \
                           main_game["f3"][0], main_game["f4"][0]))#inputs everything
    print(template3)
    for x in range(12):#for each tableau list, it checks if it is
        #the last card in the list
        #if it isnt it is replaced by an x to hide the card
        #if it is then displays the card and empty strings afterwards
        if str(main_game["tab1"][x+2]) != "  ":
            card1 = " x "            
        else:
            card1 = str(main_game["tab1"][x+1])+" "
        if str(main_game["tab2"][x+2]) != "  ":
            card2 = " x "
        else:
            card2 = str(main_game["tab2"][x+1])+" "
        if str(main_game["tab3"][x+2]) != "  ":
            card3 = " x "
        else:
            card3 = str(main_game["tab3"][x+1])+" "           
        if str(main_game["tab4"][x+2]) != "  ":
            card4 = " x "
        else:
            card4 = str(main_game["tab4"][x+1])+" "
        if str(main_game["tab5"][x+2]) != "  ":
            card5 = " x "
        else:
            card5 = str(main_game["tab5"][x+1])+" "
        if str(main_game["tab6"][x+2]) != "  ":
            card6 = " x "
        else:
            card6 = str(main_game["tab6"][x+1])+" "
        if str(main_game["tab7"][x+2]) != "  ":
            card7 = " x "
        else:
            card7 = str(main_game["tab7"][x+1])+" "
        print(template5.format(card1, card2, card3, card4, card5, card6, \
                               card7))#prints into the last template
    return main_game

def display_game(stock, waste, foundations, tabs):
    """given information on main categories prints the data in a visible way
input: the deck and waste lists, the list of foundation lists \
and the list of tabs list"""#most of it is repeated from above
    template1 = """stock waste             foundation"""#same template as above
    template2 = """{}    {}                {},{},{},{}"""
    template3 = """       tableau"""
    template5 = """{:3<} | {:3<} | {:3<} | {:3<} | {:3<} | {:3<} | {:3<}"""
    
    print(template1)
    print(template2.format(stock[0], waste[0], foundations[0][0], \
                           foundations[1][0], foundations[2][0], \
                           foundations[3][0]))
    print(template3)#names are different because it used to just import
    #from a list of lists so i just rewrote it to show it another way
    for x in range(12):#exactly the same as above 
        if str(tabs[0][x+2]) != "  ":
            card1 = "x "            
        else:
            card1 = str(tabs[0][x+1])+" "
            
        if str(tabs[1][x+2]) != "  ":
            card2 = " x "
        else:
            card2 = str(tabs[1][x+1])+" "
            
        if str(tabs[2][x+2]) != "  ":
            card3 = " x "
        else:
            card3 = str(tabs[2][x+1])+" "
            
        if str(tabs[3][x+2]) != "  ":
            card4 = " x "
        else:
            card4 = str(tabs[3][x+1])+" "
            
        if str(tabs[4][x+2]) != "  ":
            card5 = " x "
        else:
            card5 = str(tabs[4][x+1])+" "
            
        if str(tabs[5][x+2]) != "  ":
            card6 = " x "
        else:
            card6 = str(tabs[5][x+1])+" "
            
        if str(tabs[6][x+2]) != "  ":
            card7 = " x "
        else:
            card7 = str(tabs[6][x+1])+" "
            
        print(template5.format(card1, card2, card3, card4, card5, \
                               card6, card7))#yeah exactly the same
    
def stock_to_waste(stock, waste):#start of all the actual moves
    """checks if the move is valid
input: the stock and waste
output: True or False"""
    if len(stock) == 1:#checks to make sure the list isnt empty
        waste1 = waste[0]#saves that last card
        while len(waste) != 0:#goes through and refills the stock
            card = waste.pop(0)
            stock.append(card)
        card = stock.pop(0)
        waste.insert(0, card)#reinserts the last card
    else:
        card = stock.pop(0)#just changes the list around
        waste.insert(0, card)

def waste_to_foundation(waste, foundation, foundation_num):
    """checks if the move is valid
input: the waste, the list of foundation lists, and the correct list number
output: True or False"""
    card = waste[0]#saves the card to be moved
    stack = foundation[foundation_num]
    if len(stack) == 1:#checks to makes sure the stack is empty
        if card.rank() == 0:#if it isnt an ace it is rejexted
            return False
        if stack[0] == 0:
            if card.rank() == 1:
                return True
    else:
        if card.rank() == stack[0].rank()+1:#if the stack has an ace checks
            if card.suit() == stack[0].suit():#for the right suit
                return True
    return False #default rejects the card (same as all other ones)        

def waste_to_tableau(waste, tabs, c_num):
    """checks if the move is valid
input: the waste, the lists of tablaeu lists, and the correct list number
output: True or False"""
    card = waste[0]#the card to be moved
    stack = tabs[c_num]#the stack to be moved to
    count = -1
    for entry in stack:
        if str(entry) != "  ":
            count += 1#finds the position of the last card in list
    comparison_card = tabs[c_num][count]#finds the actual card
    if card.rank() == comparison_card.rank()-1:#checks to make 
        suit = card.suit()#sure its the next card
        comparison_suit = comparison_card.suit()#finds the suits
        if suit == 2 or suit == 3:#if it is the same color
            x = 1
        else:
            x = 0
        if comparison_suit == 2 or comparison_suit == 3:#as the above
            y = 1
        else:
            y = 0
        if x != y:#it only returns true if it is a different color
            return True
    return False
    
def tableau_to_foundation(tabs, foundations, c_num, f_num):
    """checks if the move is valid
input: both the lists of lists for tableau and the foundations as well\
as the correct number
output: True or False"""
    stack = tabs[c_num]
    count = -1
    for entry in stack:
        if str(entry) != "  ":
            count += 1
    card = tabs[c_num][count]#card to be moved
    comparison_card = foundations[f_num][0]#finds the card to be checked
    if comparison_card != 0:
        if card.rank() == comparison_card.rank()+1:#has to be the next card
            suit = card.suit()#in the series
            comparison_suit = comparison_card.suit()
            if suit == 1:#checks the suits
                x = 1
            elif suit == 2:
                x = 2
            elif suit == 3:
                x = 3
            elif suit == 4:
                x = 4
            else:
                print("error")

            if comparison_suit == 1:
                y = 1
            elif comparison_suit == 2:
                y = 2
            elif comparison_suit == 3:
                y = 3
            elif comparison_suit == 4:
                y = 4
            else:
                print("error")
                
            if x == y:#it has to match in order to be moved
                return True
    else:#checks for an ace
        if card.rank() == 1:
            return True
    return False

def tableau_to_tableau(tabs, c_num1, c_num2):
    """checks if the move is valid
input: the list of tableau lists and the number of which lists to check
output: True or False"""
    stack1 = tabs[c_num1]#finds the last card in the list to check
    stack2 = tabs[c_num2]
    count1 = -1
    for entry in stack1:
        if str(entry) != "  ":
            count1 += 1
    count2 = -1
    for entry in stack2:
        if str(entry) != "  ":
            count2 += 1

    if count1 == 0 or count2 == 0:#makes sure the tab isnt empty
        return True
    else:
        card = tabs[c_num1][count1]
        comparison_card = tabs[c_num2][count2]
        if card.rank() == comparison_card.rank()-1:#check if right rank
            suit = card.suit()
            comparison_suit = comparison_card.suit()
            if suit == 2 or suit == 3:#does the same check as above for suit
                x = 1
            else:
                x = 0
            if comparison_suit == 2 or comparison_suit == 3:
                y = 1
            else:
                y = 0
            if x != y:
                return True
    return False

def h():#just prints the moves
    """prints all the instructions and possible moves
input: None
output: None (executed for side effect"""
    print("""sw - move card from Stock to Waste
wf #F - move card from Waste to Foundation
wt #T - move card from Waste to Tableau
tf #T #F - move card from Tableau to Foundation
tt #T1 #T2 - move card from one tableau column to another
h - help
q - quit""")

def q():#exits out the selector
    """exits out of the selector program
input: None
output: None (executed for side effect"""
    return False

def selector(stock, waste, foundations, tabs):#calls the correct function
    """picks which program to use and if its valid moves the cards around
on an infinate loop until user enters q
input: all the parts of the game
output: True/False"""
    try:
        command = str(input("what move do you want to make? "))
        selection = command[:2]#chooses the correct function
        if selection == "sw":
            stock_to_waste(stock, waste)#calls the function
            display_game(stock, waste, foundations, tabs)#updates visials
            return True#continues the loop, same as below except for q
        
        elif selection == "wf":
            pile = int(command[3:4])-1#checks which foundation pile
            if waste_to_foundation(waste, foundations, pile) == True:
                card = waste.pop(0)#actually inserts the card
                foundations[pile].insert(0, card)
                display_game(stock, waste, foundations, tabs)
            else:
                print("Invalid move")
                display_game(stock, waste, foundations, tabs)
            return True
        
        elif selection == "wt":
            column = int(command[3:4])-1#finds the tableau pile
            if waste_to_tableau(waste, tabs, column) == True:
                count = -1
                for entry in tabs[column]:
                    if str(entry) != "  ":
                        count += 1#finds the position of the card
                card = waste[0]
                del tabs[column][count+1]
                tabs[column].insert(count+1, card)#inserts the card
                del waste[0]#deletes it from the previous list
                display_game(stock, waste, foundations, tabs)
            else:
                print("Invalid move")
                display_game(stock, waste, foundations, tabs)
            return True
        
        elif selection == "tf":
            column = int(command[3:4])-1
            found_num = int(command[5:6])-1#finds the nessessary info
            if tableau_to_foundation(tabs, foundations, column, found_num) \
               == True:
                count = -1
                for entry in tabs[column]:
                    if str(entry) != "  ":
                        count += 1
                card = tabs[column][count]#finds the position
                del tabs[column][count]
                tabs[column].insert(count+1, "  ")
                foundations[found_num].insert(0, card)#replaces the card
            else:
                print("Invalid move")
            display_game(stock, waste, foundations, tabs)
            return True
                      
        elif selection == "tt":
            column1 = int(command[3:4])-1
            column2 = int(command[5:6])-1#finds the command positions
            if tableau_to_tableau(tabs, column1, column2) == True:
                count = -1
                for entry in tabs[column1]:
                    if str(entry) != "  ":
                        count += 1
                card = tabs[column1][count]
                del tabs[column1][count]#gets rid of the previous card
                tabs[column1].insert(count, "  ")#inserts a space

                count = -1
                for entry in tabs[column2]:
                    if str(entry) != "  ":
                        count += 1
                tabs[column2].insert(count+1, card)#replaces the card
                del tabs[column2][14]#gets rid of the extra space
            else:
                print("Invalid move")
            display_game(stock, waste, foundations, tabs)
            return True
                      
        elif selection == "h":
            h()#just calls the h funciton to get credit
            return True
        elif selection == "q":
            q()#just calls the q function to get credit
        else:
            print("invalid selection")
            return True
            selection = str(input("what move do you want to make? "))
    except TypeError:#used for bug testing and invalid input commands
        print("please include the number with your selection")
        return True
    except ValueError:
        print("please include the number with your selection")
        return True
def main():
    """creates the main lists to be inputed into selector
calls the correct functions in order
input: none
output: none (executed for side effect)"""
    my_deck = cards.Deck()#creates the deck
    my_deck.shuffle()#self explanitory
    game = initial_deal(my_deck)#first function to be called
    stock = game["stock"]#next lines formats everything to be inserted into
    waste = game["waste"]#the selector function
    foundations = [game["f1"], game["f2"], game["f3"], game["f4"]]
    tabs = [game["tab1"], game["tab2"], game["tab3"], \
            game["tab4"], game["tab5"], game["tab6"], game["tab7"]]
    x = selector(stock, waste, foundations, tabs)
    while x == True:#puts it into an infinate loop until q is entered
        x = selector(stock, waste, foundations, tabs)
    print("game over")
    

main()#starts the game
