import cards


## All functions below use a "grid" containg Card instances and 0's
## The grid starts out with 20 Card instances in it.
## A Card instance is replaced with a 0 to remove it from the grid.


def create_cards_grid():
    """Returns a grid of 20 cards, all ranks between 1 and 5 (inclusive)
       The order of the cards is random (obtained from a shuffled deck) """
    new_deck = cards.Deck()
    new_deck.shuffle()
    grid = []
    count = 0
    while count < 52:
        delt_card = new_deck.deal()
        value = delt_card.rank()
        if value <= 5:
            grid.append(delt_card)
        count += 1
    return grid    

def show_grid(grid_pos1, grid_pos2, cards_grid):
    """Displays the cards_grid, revealing the cards in positions
       grid_pos1 and grid_pos2, if the positions are legal and have cards in them;
       displays all other cards as 'XX' and empty spaces as '--'   """
    template0 = "{},{},{},{}"
    key_grid = []
    for count in range(5):
        cards = 0
        row = []
        while cards < 4:
            card = cards_grid.pop()
            row.append(card)
            cards += 1
        key_grid.append(row)
    print(key_grid)
    
              
test = create_cards_grid()
show_grid(1,1,test)


def get_position():
    """Prompts the player for the row and column number of a card to turn over.
       If both are legal, it returns the corresponding grid position;
       If either is illegal, it returns a -1 """

    return -1      # replace this stub with code
            
def game_over(cards_grid):
    """Returns True if cards_grid is empty (all 0's);
       False if cards_grid contains any cards"""

    return True    # replace this stub with code



    
# finish the main logic for playing the game below this line

print("Welcome to the game of memory.\n")
tricks = ([], [])    # tricks[0] contains tricks won by player 1
                     # tricks[1] contains tricks won by player 2
                     # initially, neither player has any tricks

game = create_cards_grid()     # initialize the game

show_grid(-1, -1, game)        # display all cards face down (as XX's)

player = 1                     # start with player 1
while not game_over( game ):
    print()
    print("Player {}'s turn.".format(player))
    print("Select the first card.")
    pos1 = get_position()

    if pos1 == -1:             # change to also check that there is a card at pos1
        print("Illegal selection.  Next player's turn.")

    else:
        pass    # delete this line and add code as described below
    
        # show the grid, revealing only the card in pos1
        # get pos2 (or yield the turn, if given a bad position)
        # show the grid, revealing only the cards in pos1 and pos2
        # if the ranks match, update the grid and the player's tricks

    player = (player % 2) + 1

print("Game over.\n")

# add code to print the tricks earned by both players 
