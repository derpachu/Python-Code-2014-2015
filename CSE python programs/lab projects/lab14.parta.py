
##
## Demonstrate some of the operations of the Fraction class
##

import fraction

def display( arg1, arg2 ):

    print( "Display:", locals() )
    print()
    
    print( "arg1:", arg1 )
    print( "arg2:", arg2 )
    print()

    print( "arg1 + arg2:", arg1 + arg2 )
    print()
    print( "arg1 - arg2:", arg1 - arg2 )
    print()

    print( "arg1 == arg2:", arg1 == arg2 )
    print()
    print( "arg1 < arg2:", arg1 < arg2 )
    print()
    print( "arg1 > arg2:", arg1 > arg2 )
    print()

def main():

    A = fraction.Fraction( 3, 4)
    B = fraction.Fraction( 1, 4 )

    display( A , 5 )

main()
