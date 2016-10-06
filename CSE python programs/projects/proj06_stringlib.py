#write the following functions
#finds out if all chars are string
#finds out if all chars are numerals
#uppercases all the chars in a string
#lowercases all the chars in a string
#finds a single char and returns its location
#finds a string in a string and returns its location
#replaces a single character in a string
#replaces a string in a sring
#removes all instances where an indicated character are in a string (one char)
#same thing except the removal part can have multiple characters

def constants(selection):#all this does is make all ASCII characters refrencible
    ASCII_LOWERCASE = ("q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m")
    ASCII_UPPERCASE = ("Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M")
    DECIMAL_DIGITS = ("0,1,2,3,4,5,6,7,8,9")
    if selection == 1:
        x = ASCII_LOWERCASE
    elif selection == 2:
        x = ASCII_UPPERCASE
    elif selection == 3:
        x = DECIMAL_DIGITS
    return x
def is_alpha(x):
    if x == "":#if nothing is given then no computation is needed
        return False
    for char in x:
        if char in constants(1) or char in constants(2):
            continue#refrences all characters
        else:
            return False #continues to scan all characters but
        #if any arent in the constants then it is falase
    return True #defaults to true
def is_digit(x):
    if x == "":#same thing as above except searches through a different field
        return False
    for char in x:
        if char in constants(3):
            continue
        else:
            return False
    return True
def to_lower(x):
    end_str_list = [] #creates a new list to save the changes
    end_str = ""
    for char in x:
        if char in constants(2):#finds locations
            upper = constants(2).index(char)
            char = constants(1)[upper]
            end_str_list.append(char)#adds the corresopnding letter
            #to the other list
        else:
            end_str_list.append(char)#defaults adds all the other letters
    for letter in end_str_list:#converts list into string
        end_str += letter
    return end_str
def to_upper(x):
    end_str_list = []#same as above except the list to draw from are reversed
    end_str = ""
    for char in x:
        if char in constants(1):
            lower = constants(1).index(char)
            char = constants(2)[lower]
            end_str_list.append(char)
        else:
            end_str_list.append(char)
    for letter in end_str_list:
        end_str += letter
    return end_str
def find_chr(x,y):
    x_list = []#same strategy as above
    place = 0
    fail = -1#addes it to return if not found
    for char in x:
        x_list.append(char)#loads x into a list format
    if y =="":
        return fail#default fails if blank
    else:
        for letter in x_list:
            if letter == y:#checks every letter to see if it
                #matches what to look for
                place = x_list.index(letter)#finds the locaton
                return place
                break#to prevent it find the same letter further down
        if place == 0:#if it gets to the end without finding it it exits
            return fail
def find_str(x,y):
    x_list = []
    for char in x:
        x_list.append(char)
    fail = -1
    place = 0
    length = len(y)
    total = len(x)
    end_point = total - length
    if y == "":
        return fail
    while place < end_point:#goes through the letters until
        #it is no longer possible to have changes
        frag_list = x_list[place:place+length]
        frag = ""#makes it so it knows what to look for
        for l in frag_list:
            frag += l
        if frag == y:#finds location data and reports it
            return place
        place += 1
    if place == end_point:
            return fail
def replace_chr(x,y,z):
    x_list = []#uses the same code to find the fragments
    new_list = []
    place = 0
    replaced = ""#creates something to write the end into
    for char in x:
        x_list.append(char)
    for letter in x_list:
        place += 1
        if letter == y:
            new_list.insert(place,z)#this time it puts in z for y
        else:
            new_list += letter
    for l in new_list:#converts the list back into a string
        replaced += l
    return replaced#from now on all it will return is the replaced values
#with that method
def replace_str(x,y,z):
    x_list = []
    new_list = []
    replaced = ""
    for char in x:
        x_list.append(char)
    place = 0
    length = len(y)
    total = len(x)
    end_point = total - length#sets it up so it doesnt check if the end
    #is shorter than the thing we are looking for
    while place < end_point:
        frag_list = x_list[place:place+length]
        frag = ""
        for l in frag_list:#makes the fragment a little longer
            #to adjust for longer replacements
            frag += l
        if frag == y:
            new_list.append(z)
            x_list.pop(place+1)#keeps replacing until fragmentis used up
        else:
            new_list.append(x_list[place])
        place += 1
    for v in new_list:
        replaced +=v
    return replaced
def trim_chr(x,y):
    x_list = []
    place = 0
    replaced = ""#same as above
    for char in x:
        x_list.append(char)
    if y =="":
        return x
    else:
        for letter in x_list:
            if letter == y:
                place = x_list.index(letter)
                x_list.remove(x_list[place])#same as finding it but this time just removes it
    for l in x_list:
        replaced += l
    return replaced
def trim_all(x,y):
    x_list = []
    replaced = ""
    for char in x:
        x_list.append(char)
    fail = -1
    place = 0
    tracker = 0#needed to check how much to be removing
    length = len(y)
    total = len(x)
    end_point = total - length
    while place < end_point:#same strategy as above
        frag_list = x_list[place:place+length]
        frag = ""
        for l in frag_list:
            frag += l
        if frag == y:
            while tracker < length:
                x_list.pop(place)
                tracker += 1#here is keeps removing until the end is found
        place += 1
    for v in x_list:
        replaced +=v
    return replaced
