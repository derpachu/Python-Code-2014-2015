# Function main() implements the Lights Out game
test1 = [True, True, True]
test2 = [True, False, True]
test3 = [False, False, False, True]
test4 = [False, False, True, False]
def print_game(button_lst):
    """prints the button_lst, using '*' for "on" (True), '-' for "off" (False)   
    """
    for x in button_lst:
        if x == True:
            print(" * ", end = "")
        elif x == False:
            print(" - ", end = "")
        else:
            print("error")
#print_game(test2)
def button_on(button_lst):
    """returns True, if any button in button_lst is on (True)
       or False, if all buttons in button_lst are off (False) 
    """
    for x in button_lst:
        if x == True:
            return True
        else:
            continue
    return False
#print(button_on(test1))
#print(button_on(test2))
#print(button_on(test3))
#print(button_on(test4))
def press_button(button_lst, button_num):
    """press the given button_num in button_lst
       requires: 1 <= button_num <= len(button_lst)
       modifies: button_lst, changing the button & its neighbors
    """
    value = button_lst[button_num-1]
    if value == True:
        button_lst[button_num-1] = False
    elif value == False:
        button_lst[button_num-1] = True
    else:
        print("error")
    value_left = button_lst[button_num-2]
    if value_left == True:
        button_lst[button_num-2] = False
    elif value_left == False:
        button_lst[button_num-2] = True
    else:
        print("error")
    if button_num == len(button_lst):
        value_right = button_lst[0]
        if value_right == True:
            button_lst[0] = False
        elif value_right == False:
            button_lst[0] = True
        else:
            print("error")
    else:
        value_right = button_lst[button_num]
        if value_right == True:
            button_lst[button_num] = False
        elif value_right == False:
            button_lst[button_num] = True
        else:
            print("error")
#press_button(test1,3)
#press_button(test2,3)
#press_button(test3,4)
#press_button(test4,4)
#print(test1)
#print(test2)
#print(test3)
#print(test4)
def get_num_buttons():
    """prompts the player for the number of buttons and
       returns this number (a positive int)
    """
    num = int(input("Enter the number of buttons: "))
    return num
def get_the_button_number(num_buttons):
    """prompts the player for a button number between 1 and num_buttons
       to press, and returns the button number entered
    """
    but_num = int(input("\nEnter the number of the button to press: "))
    return but_num   
def main():
    num_buttons = get_num_buttons()
    game = [True] * num_buttons           # initially, all lights are on
    print_game(game)
    while (button_on(game)):
        button_num = get_the_button_number(num_buttons)
        press_button(game, button_num)    # updates game, pressing button_num
        print_game(game)
main()


        
        

    
    
    
