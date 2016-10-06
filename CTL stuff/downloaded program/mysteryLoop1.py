# Poorly documented program with poorly
# chosen variable names so as to remain
# a "mystery"

w = input("Enter anything: ")  #1

for c in w:  #2
    if not 'a' <= c.lower() <= 'z':  #3
        i = w.index(c)  #4
        w = w[:i]+w[i+1:]  #5

print(w) #6



