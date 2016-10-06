# Poorly documented program with poorly
# chosen variable names so as to remain
# a "mystery"
# Print statements have been added to generate
# a trace.


w = input("Enter anything: ")  #1
print("#1", end='\t')
print("w =", "'" + w + "'")

print("#2", end='\t')
for c in w:  #2
    print("c =", "'" + c + "'")
    print("#3", end=',')
    if not 'a' <= c.lower() <= 'z':  #3
        print("#4", end='\t')
        i = w.index(c)  #4
        print("i =", i)
        print("#5", end='\t')
        w = w[:i]+w[i+1:]  #5
        print("w =", "'" + w + "'")
        
    print("#2", end='\t')

print("#6")    
print(w) #6



