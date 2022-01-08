from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.ball_start()
        self.bounce = 0
        self.ball_speed = 0.03

    def ball_start(self, player=None):
            starts = [randint(120, 180), randint(0, 60), randint(180, 240), randint(300, 360)]
            select = randint(0, 3)
            self.setheading(starts[select])

    def top_check(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(360-self.heading())

    def paddle_check(self):
        self.ball_speed *= 0.95

    def new_ball(self, player=None):
        self.reset()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.ball_start(player)
        self.ball_speed = 0.04

