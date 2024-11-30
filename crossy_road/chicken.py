from turtle import Turtle

class Chicken(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(0,-280)

    def go_forward(self):
        self.forward(10)

    def reset(self):
        self.goto(0,-280)

