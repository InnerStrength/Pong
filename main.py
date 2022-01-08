from turtle import Turtle, Screen
from board import Board
from paddle import Paddle
from ball import Ball
from time import sleep

def game():
    screen = Screen()
    screen.setup(width=1000, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("Pong")


    players = []
    select = True
    while select:
        player = screen.textinput("Select Players", "Select Players:\n1 or 2 Players")
        if player == "1":
            players.append("player1")
            players.append("computer")
            select = False
        elif player =="2":
            players.append("player1")
            players.append("player2")
            select = False

    ball = Ball()
    board = Board()
    paddle = Paddle(players)
    screen.delay(10)

    game_is_on = True
    while game_is_on:
        screen.listen()
        sleep(ball.ball_speed)
        if players[1] == "computer":
            paddle.computer_move()
        else:
            screen.onkeypress(paddle.p2_move_up, "9")
            screen.onkeypress(paddle.p2_move_down, "6")
        screen.onkeypress(paddle.move_up, "w")
        screen.onkeypress(paddle.move_down, "s")
        screen.update()
        ball.top_check()
        ball.fd(10)

        for l_paddle in paddle.left_paddle:
            if -440 >= ball.xcor() >= -460 and l_paddle.distance(ball) < 10:
                ball.setheading(180 - ball.heading())
                ball.paddle_check()
                print(l_paddle.distance(ball))

        for r_paddle in paddle.right_paddle:
            if 440 <= ball.xcor() <= 460 and r_paddle.distance(ball) < 10:
                ball.setheading(180 - ball.heading())
                ball.paddle_check()
                print(r_paddle.distance(ball))

        if ball.xcor() < -500 or ball.xcor() > 500:
            board.score(ball)
            ball.new_ball()

        if board.c_score > 10:
            screen.textinput("Game Over", f"{players[1]} Wins!")
            game_is_on = False

        elif board.h_score > 10:
            screen.textinput("Game Over", f"Player 1 Wins!")
            game_is_on = False

    screen.exitonclick()

game()
