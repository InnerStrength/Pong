from turtle import Turtle,Screen

PADDLE_LENGTH=4

class Paddle(Turtle):

    def __init__(self, players):
        super().__init__()
        self.left_paddle = []
        self.right_paddle = []
        self.new_paddle(players[0])
        self.new_paddle(players[1])
        self.direction = 0

    def new_paddle(self,player):
        y = 1
        for i in range(PADDLE_LENGTH):
            self.t = Turtle()
            self.t.penup()
            self.t.color("white")
            self.t.shape("square")
            self.t.speed('fastest')
            if player == "player1":
                y = -1
            self.t.setpos(x=450 * y, y=20 * i)
            if player == "player1":
                self.left_paddle.append(self.t)
            else:
                self.right_paddle.append(self.t)

    def move_up(self):
        if self.left_paddle[-1].ycor() < 280:
            for paddle in self.left_paddle:
                paddle.setheading(90)
                paddle.fd(30)

    def move_down(self):
        if self.left_paddle[0].ycor() > -280:
            for paddle in self.left_paddle:
                paddle.setheading(270)
                paddle.fd(30)

    def p2_move_up(self):
        if self.right_paddle[-1].ycor() < 280:
            for paddle in self.right_paddle:
                paddle.setheading(90)
                paddle.fd(30)

    def p2_move_down(self):
        if self.right_paddle[0].ycor() > -280:
            for paddle in self.right_paddle:
                paddle.setheading(270)
                paddle.fd(30)

    def computer_move(self):
        if self.direction == 0 and self.right_paddle[0].ycor() > -280:
            for paddle in self.right_paddle:
                paddle.setheading(270)
                paddle.fd(20)
        else:
            self.direction = 1

        if self.direction == 1 and self.right_paddle[-1].ycor() < 280:
            for paddle in self.right_paddle:
                paddle.setheading(90)
                paddle.fd(20)
        else:
            self.direction = 0