import math  

class Point(object):
    
    def __init__(self, x_param = 0.0, y_param = 0.0):
        ''' Create a point: x_param and y_param give values for data attributes
            x and y. Defaults for both are 0.0.'''
        self.x = x_param
        self.y = y_param

    def distance (self, other): 
        """Return the distance between this Point and the other Point"""
        x_diff = self.x - other.x  # (x1 - x2)
        y_diff = self.y - other.y  # (y1 - y2)
        # square differences, sum, and take sqrt
        return math.sqrt(x_diff**2 + y_diff**2) 
    
    def sum (self, other):  
        """Return the vector Sum of this Point and the other Point"""
        new_pt = Point(self.x + other.x, self.y + other.y)
        return new_pt

    def __repr__( self ):
        x_val = round(float(self.x),1)
        y_val = round(float(self.y),1)
        return "({}, {})".format(x_val, y_val)

    def __str__ ( self ):
        return "({}, {})".format(str(self.x), str(self.y))
