#choose an option from the menu
#calculates certain functions
    #option A or a: sum of N natural numbers (include a failure message)
    #option B or b: approximate value of e
    #option C or c: approximate value of the hyperbolic sine of x (input in radians)
    #option D or d: approximate value of the hyperbolic cosine of x (input in radians)
    #option M or m: display the menu of options
    #option X or x: exit
#expand the series until the next term is less than 1.0e-7
#for B,C,D display 10 decimal points

import math

selector = input("Which option do you want: ")
while selector == 'A'\
      or selector == "a"\
      or selector == "B"\
      or selector == "b"\
      or selector == "C"\
      or selector == "c"\
      or selector == "D"\
      or selector == "d"\
      or selector == "M"\
      or selector == "m"\
      or selector == "X"\
      or selector == "x":#makes sure you select a corrent menu option
    if selector == "A" or selector == "a":
        num = int(input("Enter a natural number: "))
        x=total=0
        if num/(-1*num)==-1:#check to make sure int is not negative
            while x<num:
                x += 1
                total = total + x#summation
            print("sum of natural numbers is: ", total)
        else:
            print("Not a Natural Number")
    elif selector == "B" or selector == "b":
        Epsilon = 1.0e-7#constants and variables defined
        total = 1
        e = 1
        variable = 1/math.factorial(e)
        while variable > Epsilon:#ensures its less then epsilon constant
            variable = 1/math.factorial(e)
            total += 1/math.factorial(e)
            e += 1
        print("approximate value of e: ",round(total,10))
    elif selector == "C" or selector == "c":
        theta = float(input("enter a radian: "))#constants and variables defined
        total = 0
        Epsilon = 1.0e-7
        e = 0
        variable = theta**(2*e+1)/math.factorial(2*e+1)
        while variable > Epsilon:#ensures its less then epsilon constant
            variable = theta**(2*e+1)/math.factorial(2*e+1)
            total += theta**(2*e+1)/math.factorial(2*e+1)
            e += 1
        print("the cosh of {} is: ".format(theta),round(total,10))#round to 10
    elif selector == "D" or selector == "d":
        theta = float(input("enter a radian: "))#same as above except with cos
        total = 0
        Epsilon = 1.0e-7
        e = 0
        variable = theta**(2*e)/math.factorial(2*e)
        while variable > Epsilon:#ensures its less then epsilon constant
            variable = theta**(2*e)/math.factorial(2*e)
            total += theta**(2*e)/math.factorial(2*e)
            e += 1
        print("the cosh of {} is: ".format(theta),round(total,10))
    elif selector == "M" or selector == "m":#just prints the different options
        print("option A or a: sum of N natural numbers \
    \noption B or b: approximate value of e\
    \noption C or c: approximate value of the hyperbolic sine of x\
    \noption D or d: approximate value of the hyperbolic cosine of x\
    \noption M or m: display the menu of options\
    \noption X or x: exit)")
    elif selector == "X" or selector == "x":
        break#exits the loop upon X or x
    selector = input("Which option do you want: ")#make sure the loop can break
else:
    print("not a valid input")
print("exit")
