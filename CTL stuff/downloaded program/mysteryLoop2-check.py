# Poorly documented program with poorly
# chosen variable names so as to remain
# a "mystery"

w = input("Enter anything: ")  #1
print("#1", end='\t\t')
print("w =", "'" + w + "'")

print("#2", end='\t\t')
e = -1  #2
print("e =", e)


print("#3", end='\t\t')
m = len(w)//2  #3
print("m =", m)

print("#4", end='\t\t')
s = 0  #4
print("s =", s)

print("#5", end=',')
while s < m:  #5
    print("#6", end=',')
    if w[e]==w[s]:  #6
        print("#7", end='\t\t')
        s = s + 1  #7
        print("s =", s)
        print("#8", end='\t\t')
        e = e - 1  #8
        print("e =", e)
    else:
        print("#9", end=',')
        break  #9
    print("#5", end=',')

print("#10", end=',')
if w[e] != w[s]:  #10
    print("#11", end='\t')
    print ("Sorry, try again.")  #11
else:
    print("#12", end='\t')
    print ("Bingo!")  #12
    
