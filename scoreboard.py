from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.level = 1
            self.hideturtle()
            self.penup()
            self.goto(-280, 270)
            self.update_scoreboard()
        #Method Displays the level the user is on
        def update_scoreboard(self):
            self.clear()
            self.write(f"Level: {self.level}", align="left", font=FONT)
        #Method is called once the user has reached the finishline to increase the level
        def increase_level(self):
            self.level += 1
            self.update_scoreboard()
        #Method that displays gameover once the user collides with a car
        def gameover(self):
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=FONT)
