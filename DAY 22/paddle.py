from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        if y < 250:
            self.sety(y + 20)

    def move_down(self):
        y = self.ycor()
        if y > -240:
            self.sety(y - 20)
