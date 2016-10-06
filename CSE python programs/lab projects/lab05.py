#translate into pig latin
#does a loop until quit is entered in any capital or lower case combo
#if vowel then add way to the end
#if consonant remove all consonants until the end and add ay

initial = input("Please enter a word: ")
initial = initial.lower()

while initial != "quit":
    original = initial
    d=initial[:1]
    if d in "AEIOUaeiou":
            print(original,end="")
            print("way")
    else:
        for x in initial:
            if x in "AEIOUaeiou":
               y=int(initial.find(x))
               z=initial[:y]
               leftover=initial[y:]
               print(original, " turns into ",end="")
               print(leftover, end="")
               print(z, end="")
               print("ay")
               break
    initial = input("Please enter a word: ")
    initial = initial.lower()
print("exited")
