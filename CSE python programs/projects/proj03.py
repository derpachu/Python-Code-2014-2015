#ask if you want to process another triangle (y or Y)
#ask for dimensions
#calculate if it is a valid triangle
#shows whether it is (valid, degenerate, not a triangle)
#if valid displays
    #length of each side
    #degree measures of angles
    #radian measures of angles
    #perimeter
    #area
    #all rounded to one decimal point
#also picks if the triangle is
    #scalene
    #isosceles
    #equilateral
    #oblique
    #right
    #obtuse
#display the number of valid triangles
import math

val_tri = hyp = side1 = side2 = perimeter = area = s = 0

user = input("Do you wish to process another triangle? (Y or N) ")  
while user == "Y" or user == "y":
    a = float(input ("Enter length of side AB: "))#determines lengths
    b = float(input ("Enter length of side BC: "))
    c = float(input ("Enter length of side AC: "))
    
    round (a,1)
    round (b,1)
    round (c,1)
    
    if a>b and a>c: #picks which is the hypotenus
        hyp = a
        side1 = b
        side2 = c
    elif b>a and b>c:
        hyp = b
        side1 = a
        side2 = c
    elif c>a and c>b:
        hyp = c
        side1 = a
        side2 = b
    else:
        print ("how????")

    if side1+side2>hyp:
        print ("\tvalid triangle")
        val_tri += 1
    elif side1+side2==hyp:
        print ("\tdegenerate triangle")
    else:
        print ("\tnot a triangle")
    
    print ("Length of side AB: ", a)#reaffirms the lengths
    print ("Length of side BC: ", b)
    print ("Length of side AC: ", c)
    print ("\nDegree measure of interior angles: ")

    A = math.acos((c**2+b**2-a**2)/(2*c*b))#outputs in radians and calculates
    A1 = math.degrees(A)
    B = math.acos((a**2+c**2-b**2)/(2*a*c))
    B1 = math.degrees(B)
    C = math.acos((a**2+b**2-c**2)/(2*a*b))
    C1 = math.degrees(C)

    print ("\tAngle A: ", round (B1,1))
    print ("\tAngle B: ", round (C1,1))
    print ("\tAngle C: ", round (A1,1))

    print ("\nRadian measure of interior angles:")
    
    print ("\tAngle A: ", round (B,1))
    print ("\tAngle B: ", round (C,1))
    print ("\tAngle C: ", round (A,1))

    perimeter = a + b + c#just more calculations with formulas
    s = perimeter/2
    x = (s*(s-a)*(s-b)*(s-c))
    area = math.sqrt(x)

    print ("the perimeter is: ", perimeter)
    print ("the area is: ", area)

    if B1<90 and C1<90 and A1<90:#decides what is what
        print ("Acute Triangle")
    if B1>90 or C1>90 or A1>90:
        print ("Obtuse Triangle")
    if B1==90 or C1==90 or A1==90:
        print ("Right Triangle")
    if a==b and b==c and a==c:
        print ("Equilateral Triangle")
    if A1==B1 or B1==C1 or A1==C1:
        print ("Isoceles Triangle")
    if a!=b and b!=c and a!=c:
        print ("Scalene Triangle")
        
    user = input("Do you wish to process another triangle? (Y or N) ")
print ("Number of valid triangles: ", val_tri)
