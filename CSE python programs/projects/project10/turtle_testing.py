
import turtle

def draw_left_scaffold( pen ):
    pen.penup()
    pen.goto(0,-150)
    #Left scaffold
    pen.pendown()
    pen.goto(-50,-180)
    pen.penup()
    pen.goto(0,-150)
    pen.penup()
    #input("Press enter")
    
def draw_right_scaffold( pen ):
    #Right scaffold
    pen.pendown()
    pen.goto(50,-180)
    pen.goto(0,-150)
    pen.penup()
    #input("Press enter")
    
def draw_center_beam( pen ):
    #Center beam
    pen.pendown()
    pen.goto(0,150)
    pen.penup()
    #input("Press enter")

def draw_horizontal_beam( pen ):    
    #Horizontal beam
    pen.pendown()
    pen.goto(300,150)
    pen.penup()
    #input("Press enter")
    
def draw_rope( pen ):
    #Rope
    pen.pendown()
    pen.goto(300,100)
    pen.penup()
    #input("Press enter")
    
def draw_head( pen ):
    #Drawing head
    pen.goto(300,70)
    pen.pendown()
    pen.circle(15)
    pen.penup()
    #input("Press enter")

def draw_torso( pen ):
    #Drawing torso
    pen.pendown()
    pen.goto(300,10)
    pen.penup()
    #input("Press enter")

def draw_left_arm( pen ):
    #Drawing left arm
    pen.goto(300,40)
    pen.pendown()
    pen.goto(280,60)#Left Arm
    pen.penup()
    #input("Press enter")

def draw_right_arm( pen ):
    #Drawing right arm
    pen.goto(300,40)
    pen.pendown()
    pen.goto(320,60)#Right Arm
    pen.penup()
    #input("Press enter")

def draw_left_leg( pen ):
    #Drawing left leg
    pen.penup()
    pen.goto(300,10)
    pen.pendown()
    pen.goto(280,-10)#left leg
    pen.penup()
    #input("Press enter")

def draw_right_leg( pen ):
    #Drawing right leg
    pen.penup()
    pen.goto(300,10)
    pen.pendown()
    pen.goto(320,-10)#right leg
    pen.penup()
    #input("Press enter")

def draw_figure( pen, state ): 
    if state==1:
        draw_left_scaffold( pen )
    if state==2:
        draw_right_scaffold( pen )
    if state ==3:
        draw_center_beam( pen )
    if state ==4:
        draw_horizontal_beam( pen )
    if state ==5:
        draw_rope( pen )
    if state ==6:
        draw_head( pen )
    if state ==7:
        draw_torso( pen )
    if state ==8:
        draw_left_arm( pen )
    if state ==9:
        draw_right_arm( pen )
    if state ==10:
        draw_left_leg( pen )
    if state ==11:
        draw_right_leg( pen )
    
    
def main():
    
    # Create a Screen object (the window for the drawing)
    s = turtle.Screen()

    # Create a Turtle object (the pen to do the drawing)
    t = turtle.Turtle()

    # Clear the screen

    # Draw the eleven elements of the stick figure
    for i in range(1,12):
        draw_figure( t, i )

    # Wait for a mouse click to close the Screen object
    s.exitonclick()
    
main()

