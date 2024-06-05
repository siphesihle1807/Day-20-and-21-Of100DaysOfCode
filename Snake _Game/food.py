from turtle import Turtle
import random

# This class inherits from turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
