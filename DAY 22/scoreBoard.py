from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Left: {self.score_left} Right: {self.score_right}", align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        self.score_left += 1
        self.update_scoreboard()

    def right_point(self):
        self.score_right += 1
        self.update_scoreboard()