from turtle import Turtle, Screen
import time
from pong import Ball, Paddle
from scoreboard import Score1, Score2
from random import randint, choice
# Screen Set Up
screen = Screen()
screen.screensize(800, 600)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong!")
screen.listen()
screen.tracer(0)

ral = 0.01

line = Turtle()
line.color("white")
line.shape("square")
line.shapesize(stretch_wid=200, stretch_len=.1)

paddle_1 = Paddle()
paddle_2 = Paddle()
paddle_1.setpos(355, 0)
paddle_2.setpos(-365, 0)


screen.onkeypress(key="Up", fun=paddle_1.up)
screen.onkeypress(key="Down", fun=paddle_1.down)
screen.onkeypress(key="w", fun=paddle_2.up)
screen.onkeypress(key="s", fun=paddle_2.down)

score_1 = Score1()
score_2 = Score2()
alive = True
ball = Ball()


def game():
    screen.update()
    ball.forward(5)
    global ral
    time.sleep(ral)
    ball.bounce()
    if 360 >= ball.xcor() >= 350:
        if ball.distance(paddle_1) <= 50:
            ball.setheading(randint(110, 250))
            ral *= 0.84
        pass

    if ball.xcor() >= 390:
        score_2.update()
        ball.setpos(0, 0)
        r = choice([(55, 75), (105, 135), (235, 255), (285, 305)])
        ball.setheading(randint(*r))
        ral = 0.01

    if -370 <= ball.xcor() <= -360:
        if ball.distance(paddle_2) <= 50:
            r = choice([(290, 359), (0, 70)])
            ball.setheading(randint(*r))
            ral *= 0.84
        pass

    if ball.xcor() <= -390:
        score_1.update()
        ball.setpos(0, 0)
        r = choice([(55, 75), (105, 135), (235, 255), (285, 305)])
        ball.setheading(randint(*r))
        ral = 0.01


while alive:
    if score_2.score == 12 or score_1.score == 12:
        alive = False
    game()

screen.exitonclick()
