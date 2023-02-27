from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Current score: {self.score}",
                   align="center", font=("Arial", 24, "normal"))
        self.color = ("white")
