#this is the module that defines the legal methods in the game
#79 charaters per line
#use random module to choose a word form the list
    #but also remember to delete that word to not choose the same word twice
import turtle
import draw_hangman
import random

class PlayHangman(object):
    def __init__(self):#just initializes all variables used
        """initialize data attributes: self.__pen, self.__screen \
and self.word_list
    all other variables mentioned need to be initialized
    it also gets available words from a file called words.txt
    otherwise use a default list"""
        self.__screen = turtle.Screen()
        self.__pen = turtle.Turtle()
        self.__word = ""
        self.__used_letters = ""
        self.__display = ""
        self.__missed = 0
        self.__counter = 0
        try:#checks to see if file exists
            file = open("words.txt", "r")
            self.__word_list = []
            for line in file:
                self.__word_list.append(line)
        except FileNotFoundError:
            self.__word_list = ["computer","eskimo","beef jerky"]#default list

    def start_round(self):
        """new object of class DrawHangman save as self.__draw_hangman
    chooses a word from the list, save as self.__secret_word
    resets used letters, and number of misses and the letters correctly \
    guessed"""
        turtle.bye()
        self.__draw_hangman = draw_hangman.DrawHangman(self.__pen)
        self.__screen = turtle.Screen()
        count = random.randint(0, len(self.__word_list))
        self.__word = self.__word_list.pop(count-1)#picks the random word
        self.__word = self.__word.strip().split()
        self.__shown_word = []#what the people see
        for i in range(len(self.__word)-1):
            self.__shown_word.append("-")
        self.__counter = 0#resets the variables for the new word
        self.__used_letters = ""
        self.__missed = 0
        

    def play_letter(self, letter):
        """update the list of used letters
    update number of misses (if missed)
    update the current word (if hit)"""
        if letter in self.__used_letters:#prevents multiple guseese of the same
            print("already used that letter")#letter to trip a win early
            self.__missed += 1
            draw_hangman.DrawHangman.miss(self.__draw_hangman)
        else:
            self.__used_letters += letter#addes to the list
            if letter in self.__word:#checks to see if it is in it
                i = 0
                displayed_letter = []
                for l in self.__word:
                    if letter == l:
                        displayed_letter.append(i)#saves the locations
                    i += 1
                for x in displayed_letter:
                    self.__shown_word.pop(x)#replaces - with the letter
                    self.__shown_word.insert(x,letter)
                    self.__counter += 1
            else:
                self.__missed += 1
                draw_hangman.DrawHangman.miss(self.__draw_hangman)

    def end_of_round(self):#returns true or false
        """checks if misses are more than 11
    or
    if all the letters in the current words have been guessed"""
        if self.__missed == 11:#if you miss 12 times, game over
            return True
        if self.__counter == len(self.__shown_word):#if game won
            return True
        return False

    def get_current_word(self):#returns a list
        """returns the current word (correct guesses)
    correct letters are revealed
    hidden letters are -"""
        return self.__shown_word#list of current state of the word

    def get_used_letters(self):#return a string
        """returns a string with all the guesses made so far"""
        guesses = self.__used_letters
        return guesses

    def get_round_won(self):#returns true or false
        """returns true if round has been won
    default returns false until the game is won"""
        if self.__counter == len(self.__shown_word):#checks if all letters are 
            return True#guessed
        return False

    def words_available(self):#returns True or False
        """returns True is there are still words to guess
    if there are no more return false"""
        if len(self.__word_list) >= 1:
            return True#as long as there is one word left it will fun
        else:
            return False

    def clear_game(self):
        """calls turtle method exitonclick() at the end of the game"""
        turtle.exitonclick()#exits

