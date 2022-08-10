from turtle import Turtle
from random import randint

STARTING_POSITION = (randint(-250, 250), randint(-250, 250))

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(STARTING_POSITION)
        self.color("yellow")
        self.shape("circle")
        self.shapesize(0.5)

    def refresh(self):
        """Puts the food in a random position."""
        random_x = randint(-225, 225)
        random_y = randint(-255, 225)

        self.goto(random_x, random_y)