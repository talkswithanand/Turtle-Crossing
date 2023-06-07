import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

writeup = Turtle()
writeup.hideturtle()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
player.player_creation()

screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_creation()
    car_manager.car_move()

    # Detect collision of car and Turtle.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            writeup.write("GAME OVER", align="center", font=("courier", 30, "bold"))
            game_is_on = False

    # Detect with top edge of the screen.
    if player.is_on_top():
        player.starting_position()
        car_manager.speed_increase()
        scoreboard.update_score()



screen.exitonclick()



