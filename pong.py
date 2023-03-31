from turtle import Turtle, Screen
import random


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.setheading(90)
        self.shapesize(stretch_wid=.75, stretch_len=5)
        self.color("white")
        self.up()
        self.down()

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=.75, stretch_len=.75)
        self.color("magenta")
        self.setheading(random.randint(0, 360))
        self.bounce()

    def bounce(self):
        if self.ycor() <= -280:
            if 270 <= self.heading() <= 359:
                self.setheading(90 - (self.heading() - 270))
            else:
                self.setheading((180 - (self.heading() - 90)) + 90)

        if self.ycor() >= 280:
            if 0 <= self.heading() <= 90:
                self.setheading(270 + (90 - self.heading()))
            else:
                self.setheading(180 + (180 - self.heading()))






# Fucked Up Code / Good Efforts Tho!


# class Pong(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.move()
#         self.paddle_1 = Turtle()
#         self.paddle_2 = Turtle()
#         self.paddle_1.shape("square")
#         self.paddle_2.shape("square")
#         self.paddle_1.pu()
#         self.paddle_2.pu()
#         self.paddle_1.setheading(90)
#         self.paddle_2.setheading(90)
#         self.paddle_1.shapesize(stretch_wid=1, stretch_len=5)
#         self.paddle_2.shapesize(stretch_wid=1, stretch_len=5)
#         self.paddle_1.color("white")
#         self.paddle_2.color("white")
#         self.paddle_1.setpos(380, 0)
#         self.paddle_2.setpos(-380, 0)
#
#     def move(self):
#         screen = Screen()
#
#         def up():
#             self.paddle_1.forward(20)
#
#         def down():
#             self.paddle_1.backward(20)
#
#         screen.onkeypress(key="Up", fun=up)
#         screen.onkeypress(key="Down", fun=down)
#         def arriba():
#             self.paddle_2.forward(20)
#         def abajo():
#             self.paddle_2.backward(20)
#         screen.onkeypress(key="w", fun=arriba)
#         screen.onkeypress(key="s", fun=abajo)
#
#     # def point(self)
#     #     if ball.xcor >

