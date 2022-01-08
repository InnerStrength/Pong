from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 20, "normal")

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.h_score = 0
        self.c_score = 0
        self.left_turtle()
        self.right_turtle()
        self.draw_board()

    def right_turtle(self):
        self.right = Turtle()
        self.right.speed("fast")
        self.right.hideturtle()
        self.right.setpos(70, 250)
        self.right.color("white")
        self.computer_score()

    def left_turtle(self):
        self.left = Turtle()
        self.left.hideturtle()
        self.left.speed('fast')
        self.left.setpos(-75, 250)
        self.left.color("white")
        self.left_score()

    def left_score(self):
        self.left.write(self.h_score, align=ALIGNMENT, font=FONT)

    def computer_score(self):
        self.right.write(self.c_score, align=ALIGNMENT, font=FONT)

    def add_h_score(self):
        self.h_score += 1
        self.left.clear()
        self.left_score()

    def add_c_score(self):
        self.c_score += 1
        self.right.clear()
        self.computer_score()

    def draw_board(self):
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.setpos(0,310)
        self.setheading(270)
        for _ in range(30):
            self.fd(10)
            self.penup()
            self.fd(10)
            self.pendown()

    def score(self,ball):
        if ball.xcor() <= -480:
            self.add_c_score()
        elif ball.xcor() >= 480:
            self.add_h_score()
