#this program actually calls the turtle to draw the hangman
#79 characters
import turtle

class DrawHangman:
    def __init__(self, pen):
        """initiallize self.__pen and self.__state
self.state keeps track of how much has been drawn"""
        self.__pen = turtle.Turtle()#initializing variables
        self.__state = 0

    def miss(self):
        """increments the __state
 drawes the figure"""
        self.__state += 1#finds the state

        if self.__state == 1:
            self.__pen.penup()#draws left part of scaffold
            self.__pen.goto(0,-150)
            self.__pen.pendown()
            self.__pen.goto(-50,-180)
            self.__pen.penup()
            self.__pen.goto(0,-150)
            self.__pen.penup()
        if self.__state == 2:
            self.__pen.pendown()#draws right part of scaffold
            self.__pen.goto(50,-180)
            self.__pen.goto(0,-150)
            self.__pen.penup()
        if self.__state == 3:
            self.__pen.pendown()#draws the center beam
            self.__pen.goto(0,150)
            self.__pen.penup()
        if self.__state == 4:
            self.__pen.pendown()#draws the cross bar
            self.__pen.goto(300,150)
            self.__pen.penup()
        if self.__state == 5:
            self.__pen.pendown()#draws the rope
            self.__pen.goto(300,100)
            self.__pen.penup()
        if self.__state == 6:
            self.__pen.goto(300,70)#draws head
            self.__pen.pendown()
            self.__pen.circle(15)
            self.__pen.penup()
        if self.__state == 7:
            self.__pen.down()#draws the body
            self.__pen.goto(300,10)
            self.__pen.penup()
        if self.__state == 8:
            self.__pen.goto(300,40)#draws left arm
            self.__pen.pendown()
            self.__pen.goto(280,60)
            self.__pen.penup()
        if self.__state == 9:
            self.__pen.goto(300,40)#draws right arm
            self.__pen.pendown()
            self.__pen.goto(320,60)
            self.__pen.penup()
        if self.__state == 10:
            self.__pen.penup()#draws left leg
            self.__pen.goto(300,10)
            self.__pen.pendown()
            self.__pen.goto(280,-10)
            self.__pen.penup()
        if self.__state == 11:
            self.__pen.penup()#draws right leg
            self.__pen.goto(300,10)
            self.__pen.pendown()
            self.__pen.goto(320,-10)
            self.__pen.penup()
        
