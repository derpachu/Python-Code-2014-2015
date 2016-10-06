import math

class Vector (object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__ (self):
        return "({},{})".format(self.__x, self.__y)

    def __str__ (self):
        string1 = str(self.__x)
        string2 = str(self.__y)
        return string1 + "," + string2
    
    def magnitude (self):
        x = self.__x
        y = self.__y
        added = x**2 + y**2
        magnitude = float(math.sqrt(added))
        return magnitude

    def __add__ (self, other):
        if type(other) != Vector:
            other = Vector(other)
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Vector(x,y)
    
    def __sub__(self, other):
        if type(other) != Vector:
            other = Vector(other)
        x = self.__x + (-1)*other.__x
        y = self.__y + (-1)*other.__y
        return Vector(x,y)

    def __mul__ (self, other):
        if type(other) == float:
            x = self.__x * other
            y = self.__y * other
            return Vector(x,y)
        if type(self) == Vector and type(other) == Vector:
            dot_prod = self.__x * other.__x + self.__y * other.__y
            return dot_prod

    def __rmul__(self, other):
            x = other * self.__x
            y = other * self.__y
            return Vector(x,y)

    def __eq__(self, other):
        if self.__x == other.__x and self.__y == other.__y:
            return True
        else:
            return False

