#class time
#__hour, __mins, __secs

class time(object):
    def __init__ (self, hour = 0, mins = 0, secs = 0):
        """It sets the three instance variables to real variables to be used"""
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs

    def __repr__ (self):
        """allows the variable created to show real data"""
        template = "Class Time: {:02d}:{:02d}:{:02d}".format(self.__hour, self.__mins, self.__secs)
        return template
    
    def __str__ (self):
        """if the class is called in a print function allows it to be readable"""
        template = "{:02d}:{:02d}:{:02d}".format(self.__hour, self.__mins, self.__secs)
        return template

    def from_str (self, str_time):
        """allows a time variable to be formed when given a string"""
        hour, mins, secs = [int(n) for n in str_time.split(":")]
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs
