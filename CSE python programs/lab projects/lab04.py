#if input is squared
    #Input initial integer number
    #Input series limit

    #output x^2+(x+1)^2....(x+n)^2)
#if input is cubed
    #Input initial integer number
    #Input series limit

    #output x^3+(x+1)^3....(x+n)^3)
#outputs "***Invalid choice***" otherwise

exponent = input("please enter squared or cubed: ")
while exponent == "squared" or exponent == "cubed":
    x = int(input("Initial integer number: "))
    y = int(input("Number of Terms: "))
    counter = total = 0
    if exponent == "squared":
        while counter < y:
            total += x**2
            x = x+1
            counter += 1
    if exponent == "cubed":
        while counter < y:
            total += x**3
            x = x+1
            counter += 1
    print("Squared sum is: ", total)
    exponent = input("please enter squared or cubed: ")
else:
    print("***Invalid Choice***")
