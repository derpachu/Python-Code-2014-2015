class Drink (object):
 
    def __init__( self, price=0 ):
        print("#1"); self.price = price;         #1
        print("#2"); self.kind = "Drink"         #2

    def __str__( self ):
        print("#3"); return "{} @ $ {:0.2f}".\
                     format( self.kind,
                             self.price );       #3

    def __repr__( self ):
        print("#4"); return str( self )          #4

    def get_price( self ):      
        print("#5"); return self.price           #5

    def get_kind( self ):             
        print("#6"); return self.kind            #6

    def print_price_sticker( self ): 
        print("#7"); print( self.get_kind() )    #7
        print("#8"); print( "Price: {:0.2f}".format(
            self.get_price() ) )     #8


class CocaCola (Drink):

    def __init__(self):
        print("#9"); Drink.__init__(self,1.25)         #9
        print("#10"); self.kind = "Coca-Cola Classic"  #10


class Milk ( Drink ):

    def __init__( self, percent_fat=0 ):
        print("#11"); Drink.__init__(self, 0.75);      #11
        print("#12"); self.kind = "Milk"               #12
        print("#13"); self.percent_fat = percent_fat;  #13

    def __str__( self ):
        print("#14"); milk_str = Drink.__str__( self ) #14
        print("#15"); fat_str = " ({} % fat)".format(
            self.get_fat() )                           #15
        print("#16"); return milk_str + fat_str        #16

    def get_fat(self): 
        print("#17"); return self.percent_fat          #17

    def print_price_sticker( self ):    
        print("#18"); print( "{} {}%".format(
            self.get_kind(),
            self.get_fat() ) )           #18
        print("#19"); print( "Price: {:0.2f}".format(
            self.get_price() ) )         #19

class ChocolateMilk( Milk ):

    def __init__( self, percent_fat=0 ):
        print("#20"); Milk.__init__( self, percent_fat) #20
        print("#21"); self.kind = "Chocolate Milk"      #21

class WhiteMilk( Milk ):

    def __init__( self, percent_fat=0 ):
        print("#22"); Milk.__init__( self, percent_fat) #22
        print("#23"); self.kind = "White Milk"          #23

        
d = Drink()
print("d:", d, "\n")
d.print_price_sticker( )
print()

d = CocaCola( )
print("d:", d, "\n")
d.print_price_sticker( )
print()

d = Milk()
print("d:", d, "\n")
d.print_price_sticker( )
print()

d = Milk( 1 )
print("d:", d, "\n")
d.print_price_sticker( )
print()

d = ChocolateMilk( 2 )
print("d:", d, "\n")
d.print_price_sticker( )
print()



        
        

        
            
    
