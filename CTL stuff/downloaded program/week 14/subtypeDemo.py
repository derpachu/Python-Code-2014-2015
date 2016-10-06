from drinks import *

generic_drink = Drink()
coke = CocaCola()
milk = Milk( 2 )
choc_milk = ChocolateMilk()

print( "type( generic_drink ):", end=" " )
print( type( generic_drink ) )     # Prints:__________________
print( "type( coke ):", end=" " )
print( type( coke ) )              # Prints:__________________
print( "type( milk ):", end=" " )
print( type( milk ) )              # Prints:__________________
print( "type( choc_milk ):", end=" " )
print( type( choc_milk ) )         # Prints:__________________
print()

print( "isinstance( generic_drink, Drink):", end=" " )
print( isinstance(generic_drink, Drink) )        # Prints:________

print( "isinstance( coke, Drink ):" , end=" ")
print( isinstance( coke, Drink ) )               # Prints:________

print( "isinstance( generic_drink, CocaCola ):", end=" " )
print( isinstance( generic_drink, CocaCola ) )   # Prints:________

print( "isinstance( choc_milk, Drink ):", end=" " )
print( isinstance( choc_milk, Milk ) )           # Prints:________

print( "isinstance( milk, ChocolateMilk ):", end=" " )
print( isinstance( milk, ChocolateMilk ) )       # Prints:________

print( "isinstance( choc_milk, CocaCola ):", end=" " )
print( isinstance( choc_milk, CocaCola ) )       # Prints:________

print( "isinstance( choc_milk, WhiteMilk ):", end=" " )
print( isinstance( choc_milk, WhiteMilk ) )      # Prints:________

print( "isinstance( choc_milk, object ):", end=" " )
print( isinstance( choc_milk, object ) )         # Prints:________

print( "isinstance( Milk, Drink ):", end=" " )
print( isinstance( Milk, Drink ) )               # Prints:________

print( "isinstance( Milk, type ):", end=" " )
print( isinstance( Milk, type ) )                # Prints:________








