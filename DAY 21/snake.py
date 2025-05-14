from turtle import Turtle

MOVE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)
        self.head.forward(MOVE)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
