import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        x_coord = random.randint(-280, 280)
        y_coord = random.randint(-280, 280)
        self.goto(x_coord, y_coord)

