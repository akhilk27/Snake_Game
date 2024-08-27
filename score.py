from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 267)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Roboto", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", align="center", font=("Roboto", 28, "normal"))

