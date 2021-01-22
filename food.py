from turtle import Turtle
import random

MAX_VAL = 255       #COORDINATES ADJUSTED DEPENDING ON THE BORDER
MIN_VAL = -255


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)  #MAKE IT HALF THE DEFAULT SIZE
        self.speed("fastest")
        self.color('blue')
        self.new_position()

    def new_position(self):
        #GENERATE RANDOM POSITION WITHIN THE BORDER TO PLACE THE NEW FOOD AT
        rand_x = random.randint(MIN_VAL,MAX_VAL)
        rand_y = random.randint(MIN_VAL,MAX_VAL)
        self.goto(rand_x,rand_y)
