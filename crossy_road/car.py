from turtle import Turtle
import random
colors = [
    "red", "blue", "green", "yellow", "purple",
    "orange", "pink", "brown", "cyan", "magenta",
    "lime", "indigo", "gold", "teal", "violet"
]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars=[]
        self.start = 5
        self.increment = 2


    def move(self):
        for car in self.cars:
            car.backward(self.start)

    def create(self):
        chance=random.randint(0,6)
        if chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y=random.randint(-240,250)
            new_car.goto(300,random_y)
            self.cars.append(new_car)


    def reset(self):

        self.start+=self.increment













