
################################################################################
## Demonstration program for class Date
################################################################################

import date

A = date.Date( 1, 1, 2014 )

print( A )
print( A.to_iso() )
print( A.to_mdy() )
print( A.is_valid() )
print()

B = date.Date( 12, 31, 2014 )

print( B )
print( B.to_iso() )
print( B.to_mdy() )
print( B.is_valid() )
print()

C = date.Date()

C.from_iso( "2014-07-04" )

print( C )
print( C.to_iso() )
print( C.to_mdy() )
print( C.is_valid() )
print()

D = date.Date()

D.from_mdy( "March 15, 2015" )

print( D )
print( D.to_iso() )
print( D.to_mdy() )
print( D.is_valid() )
print()

E = date.Date()

print( E )
print( E.to_iso() )
print( E.to_mdy() )
print( E.is_valid() )
print()

test1 = date.Date()
test2 = date.Date()
test3 = date.Date()
test4 = date.Date()
test5 = date.Date()
##test1 = date.Date( 1d, 40, 6124 )
##test2.from_iso("ab cd efgh")
##test3.from_mdy("ab cd efgh")
##test4.from_iso(13, 40, 6124)
##test5.from_mdy(13, 40, 6124)
##print(test1)
##print(test2)
##print(test3)
##print(test4)
##print(test5)
