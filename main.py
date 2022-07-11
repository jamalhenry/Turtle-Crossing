import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#Initializing the imported classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
#Enabling turtle movement with the up arrow on the keyboard
screen.listen()
screen.onkey(player.move_turtle, "Up")
#While loop that updates the animation and start the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Create the cars
    car_manager.create_car()
    #Establish movement of the cars
    car_manager.move_cars()

    #Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

    #Detect a seuccessful crowwing
    if player.finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()




#Once exiting the loop the user can click the screen to exit the program
screen.exitonclick()