# Poorly documented program with poorly
# chosen variable names so as to remain
# a "mystery"

w = input("Enter anything: ")  #1

e = -1  #2
m = len(w)//2  #3
s = 0  #4
while s < m:  #5
    if w[e]==w[s]:  #6
        s = s + 1  #7
        e = e - 1  #8
    else:
        break  #9

if w[e] != w[s]:  #10
    print ("Sorry, try again.")  #11
else:
    print ("Bingo!")  #12
    
