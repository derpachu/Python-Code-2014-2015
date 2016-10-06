
import play_hangman

game = play_hangman.PlayHangman()

user_input = 'yes'
while user_input.lower() != 'no' and  user_input.lower() != 'n':
    
    game.start_round()
    print( "\nThe secret word: ", game.get_current_word() )
    
    while not game.end_of_round():
        
        user_input_char = input( "\nChoose a letter: " )
        game.play_letter( user_input_char.lower() )
        
        print( "\n  Current word: ", game.get_current_word() )
        print( "\n  Used letters: ", game.get_used_letters() )
        
    if game.get_round_won():
        print( "\nCongratulations! You guessed the word." )
    else:
        print( "\nSorry! You lost that round." )
        
    if not game.words_available():
        print( "\nGame over -- no more words available." )
        break
    
    user_input = input( "\nWould you like to play another round (y/n)? " )
    
else:
    print( "\nClick on the turtle window to exit." )
    game.clear_game()
