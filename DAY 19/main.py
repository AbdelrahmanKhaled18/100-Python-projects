import random
from turtle import Screen, Turtle

""""
tim = Turtle()
screen = Screen()


#making etch sketch game

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
"""

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=100 - (i * 30))  # Position turtles
    turtles.append(turtle)  # Add turtle to the list

the_race_on = False
if user_bet:
    the_race_on = True

while the_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            the_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
