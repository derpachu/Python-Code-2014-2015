#create a class to do methods
#1 oz = 29.5735295625 ml
#79 chars
#NO FUNCTION HAS PRINT
#all comparison
    #picks a unit to add if different units are added
    #return false if object is invalid
    #==
    #!=
    #<
    #<=
    #>
    #>=
#+-*
    #picks a unit to add if different units are added
    #no alterations to the original object
    #if object is invalid, method returns invalid object


class Volume(object):
    def __init__(self, mag=0, unit="ml"):#initializes
        """default (0,"ml")"""
        
        self.__mag = 0#sets defaults if invalid inputs
        self.__unit = "ml"
        
        if type(mag) == float and type(unit) == str:#sets values if valid
            self.__mag = mag
            self.__unit = unit
        
    def is_valid(self):
        """returns bool if valid"""
        if type(self) != Volume:#auto returns false if object is not Volume
            return False
        elif type(self.__mag) == float and type(self.__unit) == str:
            return True#inputs have to be right
        else:
            return False
        
    def __repr__(self):
        """return "Not a Volume" if invalid"""
        if self.is_valid() == True:#checks to make sure its correct
            return "Volume: {}, unit: {}".format(self.__mag, self.__unit)
        else:
            return "Not a Volume"
        
    def __str__(self):
        """return "Not a Volume" if invalid"""
        if self.is_valid() == True:#prints it
            return "{} {}".format(self.__mag, self.__unit)
        else:
            return "Not a Volume"
        
    def units(self):
        """return the unit "ml" or "oz"""
        if self.is_valid() == True:
            return self.__unit#just returns that position
        else:
            return "Not a Volume"
        
    def magnitude(self):
        """return the value"""
        if self.is_valid() == True:
            return float(self.__mag)#same as above
        else:
            return "Not a Volume"
        
    def metric(self):
        """return the value in 'ml'"""
        if self.is_valid() == True:
            if self.__unit == "ml":#if its already in metric returns same
                return "{} ml".format(self.__mag)
            if self.__unit == "oz":
                converted = self.__mag * 29.5735295625#converts
                return converted
            else:
                return "Not a Volume"
        else:
            return "Not a Volume"
        
    def customary(self):
        """return the value in 'oz'"""
        if self.is_valid() == True:
            if self.__unit == "oz":#if its already in customary returns same
                return "{} oz".format(self.__mag)
            if self.__unit == "ml":
                converted = self.__mag / 29.5735295625#converts
                return converted
            else:
                return "Not a Volume"
        else:
            return "Not a Volume"
    def __eq__(self, other):
        if type(other) != Volume or type(self) != Volume:
            return False#if invalid objects returns false
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                if self.__mag == other.__mag:#if same unit direct comparison
                    return True
                else:
                    return False
            elif self.__unit == "oz" and other.__unit == "oz":
                if self.__mag == other.__mag:#same as above
                    return True
                else:
                    return False
            else:
                if self.__unit == "oz":#converts that side to metric
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625#same
                    x = self.__mag
                if x == y:
                    return True
                else:
                    return False
            
    def __ne__(self, other):#all comparison functions follow same pattern
        if type(self) != Volume or type(other) != Volume:
            return False
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                if self.__mag != other.__mag:
                    return True
                else:
                    return False
            elif self.__unit == "oz" and other.__unit == "oz":
                if self.__mag != other.__mag:
                    return True
                else:
                    return False
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                if x != y:
                    return True
                else:
                    return False
            
    def __le__(self,other):#all comparison functions follow same pattern
        if type(other) != Volume or type(self) != Volume:
            return False
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                if self.__mag <= other.__mag:
                    return True
                else:
                    return False
            elif self.__unit == "oz" and other.__unit == "oz":
                if self.__mag <= other.__mag:
                    return True
                else:
                    return False
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                if x <= y:
                    return True
                else:
                    return False
            
    def __ge__(self,other):#all comparison functions follow same pattern
        if type(other) != Volume or type(self) != Volume:
            return False
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                if self.__mag >= other.__mag:
                    return True
                else:
                    return False
            elif self.__unit == "oz" and other.__unit == "oz":
                if self.__mag >= other.__mag:
                    return True
                else:
                    return False
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                if x >= y:
                    return True
                else:
                    return False
            
    def __lt__(self,other):#all comparison functions follow same pattern
        if type(other) != Volume or type(self) != Volume:
            return False
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                if self.__mag < other.__mag:
                    return True
                else:
                    return False
            elif self.__unit == "oz" and other.__unit == "oz":
                if self.__mag < other.__mag:
                    return True
                else:
                    return False
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                if x < y:
                    return True
                else:
                    return False
            
    def __gt__(self,other):#all comparison functions follow same pattern
        if type(other) != Volume or type(self) != Volume:
            return False
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                if self.__mag > other.__mag:
                    return True
                else:
                    return False
            elif self.__unit == "oz" and other.__unit == "oz":
                if self.__mag > other.__mag:
                    return True
                else:
                    return False
            else:
                if self.__unit == "oz":
                    x = self.__mag/29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag/29.5735295625
                    x = self.__mag
                if x > y:
                    return True
                else:
                    return False

    def __add__(self,other):
        if type(self) != Volume or type(other) != Volume:
            return "Invalid object"#kills if not valid objects to add
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                added = self.__mag + other.__mag#if same directly addes
                return added
            elif self.__unit == "oz" and other.__unit == "oz":
                added = self.__mag + other.__mag#if same directly addes
                return added
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625#converts
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625#converts
                    x = self.__mag
                added = x+y#directly addes
                return added

    def __radd__(self,other):#directly the same as above
        if type(self) != Volume or type(other) != Volume:
            return "Invalid object"
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                added = self.__mag + other.__mag
                return added
            elif self.__unit == "oz" and other.__unit == "oz":
                added = self.__mag + other.__mag
                return added
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                added = x+y
                return added

    def __sub__(self,other):#follows __add__ patern but with -
        if type(self) != Volume or type(other) != Volume:
            return "Invalid object"
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                subbed = self.__mag - other.__mag
                return subbed
            elif self.__unit == "oz" and other.__unit == "oz":
                subbed = self.__mag - other.__mag
                return subbed
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                subbed = x-y
                return subbed

    def __rsub__(self,other):#directly the same as above
        if type(self) != Volume or type(other) != Volume:
            return "Invalid object"
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                subbed = self.__mag - other.__mag
                return subbed
            elif self.__unit == "oz" and other.__unit == "oz":
                subbed = self.__mag - other.__mag
                return subbed
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                subbed = x-y
                return subbed

    def __mul__(self,other):#follows __add__ patern but with *
        if type(self) != Volume or type(other) != Volume:
            return "Invalid object"
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                mul = self.__mag * other.__mag
                return mul
            elif self.__unit == "oz" and other.__unit == "oz":
                mul = self.__mag * other.__mag
                return mul
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                mul = x*y
                return mul
        
    def __rmul__(self,other):#directly the same as above
        if type(self) != Volume or type(other) != Volume:
            return "Invalid object"
        else:
            if self.__unit == "ml" and other.__unit == "ml":
                mul = self.__mag * other.__mag
                return mul
            elif self.__unit == "oz" and other.__unit == "oz":
                mul = self.__mag * other.__mag
                return mul
            else:
                if self.__unit == "oz":
                    x = self.__mag*29.5735295625
                    y = other.__mag
                else:
                    y = other.__mag*29.5735295625
                    x = self.__mag
                mul = x*y
                return mul
