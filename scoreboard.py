from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220,240)
        self.score = 1
        self.show_score()
    def show_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
    def update_score(self):
        self.score += 1
        self.show_score()
    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font = ("Courier", 30,"normal"))
