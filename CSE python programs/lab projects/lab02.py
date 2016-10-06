import math

a_value = float ( input ("Enter A: "))
b_value = float ( input ("Enter B: "))
c_value = float ( input ("Enter C: "))

root_a = (((-b_value + math.sqrt(b_value**2-4*(a_value)*(c_value))))/(2*a_value))
root_b = (((-b_value - math.sqrt(b_value**2-4*(a_value)*(c_value))))/(2*a_value))

print ("The first root is: ", root_a)
print ("The second root is: ", root_b)
