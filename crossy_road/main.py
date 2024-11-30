from turtle import Screen
import time
from chicken import Chicken
from level_board import Score_board
from car import Car

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

chicken = Chicken()
score_board = Score_board()
car_manager = Car()

screen.listen()
screen.onkey(chicken.go_forward, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    car_manager.create()  # Create cars at intervals
    car_manager.move()   # Move all cars
    screen.update()

    # Collision detection and game logic go here
    for car in car_manager.cars:
        if chicken.distance(car)<30:
            score_board.select_color()
            score_board.game_over()
            game_on=False
    # Example: Increase speed at certain conditions
    if chicken.ycor()>290:
        score_board.level_up()
        chicken.reset()
        car_manager.reset()






screen.exitonclick()
