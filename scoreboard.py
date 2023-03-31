from turtle import Turtle


class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(40, 240)
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=('Arial', 25, 'normal'))
        self.score += 1
        if self.score == 12:
            self.game_over()

    def game_over(self):
        self.color("white")
        self.pu()
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER!", align="center", font=('Arial', 25, 'normal'))


class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(-40, 240)
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=('Arial', 25, 'normal'))
        self.score += 1
        if self.score == 12:
            self.game_over()


    def game_over(self):
        self.color("white")
        self.pu()
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER!", align="center", font=('Arial', 25, 'normal'))
