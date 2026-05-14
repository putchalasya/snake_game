from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ranx=random.randint(-280,280)
        rany=random.randint(-280,280)
        self.goto(ranx,rany)


    
