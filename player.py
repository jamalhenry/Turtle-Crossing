STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    #Designing the turtle
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.go_to_start()
        self.left(90)

    #Method that moves the turtle
    def move_turtle(self):
        self.forward(MOVE_DISTANCE)
    #Method that returns the turtle to the starting point after getting to the finishline
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    #Method that detects the Finishline
    def finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

