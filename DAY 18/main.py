###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


# drawing 10x10 dots painting
def draw_dot_painting():
    turtle.colormode(255)
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)

    for i in range(10):
        for j in range(10):
            random_color = random.choice(rgb_colors)
            turtle.dot(20, (random_color.r, random_color.g, random_color.b))
            turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
        turtle.left(90)
        turtle.forward(50)
        turtle.setheading(0)


# main function
def main():
    draw_dot_painting()
    turtle.exitonclick()

if __name__ == "__main__":
    main()