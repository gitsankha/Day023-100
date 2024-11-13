import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""Difficulty level . The more numbers there are in the
INTERVALS the more the cars will get generated and the game will get harder"""
INTERVALS = [3,5,10,13,15,17]

#Initial screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


#create a Player object
player = Player()


#create a scoreboard object
scoreboard = Scoreboard()


#create a bunch of car
car_manager = CarManager()


#bind "Up" key with the turtle's going up
screen.onkeypress(player.move_up, "Up")


i = 1
game_is_on = True
while game_is_on:
    random_interval = random.choice(INTERVALS)
    screen.update()
    time.sleep(0.1)
    if player.is_goal_reached():
        scoreboard.update_score()
        car_manager.increase_car_speed()
    car_manager.move_cars()
    if i % random_interval == 0:
        car_manager.generate_new_car()
    i += 1
    for car in car_manager.cars_list:
        if player.distance(car) < 27:
            scoreboard.game_over()
            game_is_on = False
#todo manage car maneger well



screen.exitonclick()