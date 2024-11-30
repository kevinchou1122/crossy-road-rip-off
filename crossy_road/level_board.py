from turtle import Turtle
import random

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-280,260)
        self.level=1
        self.write(f"Level: {self.level}",align="left",font=("Arial",28,"normal"))



    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}", align="left", font=("Arial", 28, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 80, "normal"))

    def select_color(self):
            self.color("red")