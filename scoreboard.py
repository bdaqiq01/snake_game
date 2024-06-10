from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()

    def add_score(self):
        self.score += 1
    def show_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Ariel", 24, "normal"))



