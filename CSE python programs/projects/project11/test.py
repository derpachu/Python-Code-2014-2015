import volume

#this is to test every method in class volume is implimented correctly

a = volume.Volume(10.0, "oz")#creates the variables
a_copy = volume.Volume(10.0, "oz")
b = volume.Volume(295.7, "ml")
c = volume.Volume(10.0, "ml")
d = volume.Volume(0.3, "oz")
bad = volume.Volume("ml", 12.0)
wrong = "wrong"

print("a: ",a)#shows all the variables
print("b: ",b)
print("c: ",c)
print("d: ",d)
print("bad: ",bad)
print("wrong: wrong")
print()

print("a.units(): ", a.units())#tests units function
print("b.units(): ", b.units())
print("bad.units(): ", bad.units())
print("volume.Volume('pqr',5).units(): ", volume.Volume('pqr',5).units())
print()

print("c.magnitude(): ", c.magnitude())#test magnitude
print("d.magnitude(): ", d.magnitude())
print("bad.magnitude(): ", bad.magnitude())
print("volume.Volume('pqr',5).magnitude(): ", \
      volume.Volume('pqr',5).magnitude())
print()

print("c.metric(): ", c.metric())#test metric
print("d.metric(): ", d.metric())
print("bad.metric(): ", bad.metric())
print("volume.Volume('pqr',5).metric(): ", volume.Volume('pqr',5).metric())
print()

print("a.customary(): ", a.customary())#test customary
print("b.customary(): ", b.customary())
print("bad.customary(): ", bad.customary())
print("volume.Volume('pqr',5).customary(): ", \
      volume.Volume('pqr',5).customary())
print()

print("a == b: ", a == b)#test eq
print("a == a_copy", a == a_copy)
print("b == d: ", b == d)
print("bad == a: ", bad == a)
print("wrong == a: ", wrong == a)
print()

print("c != a: ", c != a)#test ne
print("a != b: ", a != b)
print("a != a_copy: ", a != a_copy)
print("bad != a: ", bad != a)
print("wrong != a: ", wrong != a)
print()

print("a >= b: ", a >= b)#test the comparisons
print("a >= a_copy: ", a >= a_copy)
print("a >= c: ", a >= c)
print("wrong <= a: ", wrong <= a)
print("a > b: ", a > b)
print("a > c: ", a > c)
print("wrong > a: ", wrong > a)
print("a <= b: ", a <= b)
print("a <= a_copy: ", a <= a_copy)
print("a <= c: ", a <= c)
print("wrong <= a: ", wrong <= a)
print("a < b: ", a < b)
print("a < c: ", a < c)
print("wrong < a: ", wrong < a)
print()

print("a+b: ", a+b)#test add
print("d+a: ", d+a)
print("a+c: ", a+c)
print("bad+a: ", bad+a)
print("wrong + a: ", wrong + a)
print()

print("a-b: ", a-b)#test sub
print("b-c: ", b-c)
print("a-c: ", a-c)
print("a-bad: ", a-bad)
print("wrong - a: ", wrong - a)
print()

print("a*b: ", a*b)#test mul
print("d*a: ", d*a)
print("a*c: ", a*c)
print("bad*a: ", bad*a)
print("wrong * a: ", wrong * a)

