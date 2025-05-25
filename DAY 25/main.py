import turtle
import pandas
from turtle import *

""""
temp = []
with open("weather_data.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        if row[1] == "temp":
            continue
        temp.append(int(row[1]))
        print(row)

print(temp)
"""

# print(pd.read_csv("weather_data.csv")["temp"].sum() / len(pd.read_csv("weather_data.csv")["temp"].tolist()))

"""
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

print(pd.DataFrame(data_dict).to_csv("count.csv", index=False))
"""
# Initial setup
counter = 0
guessed_states = []

# Load state data
data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

# Setup screen and background image
screen = Screen()
screen.title("US States Map")
screen.addshape("blank_states_img.gif")

background_turtle = Turtle()
background_turtle.shape("blank_states_img.gif")

# Turtle for writing state names
label_turtle = Turtle()
label_turtle.hideturtle()
label_turtle.penup()

# Main game loop
while counter < 50:
    answer = screen.textinput(f"{counter}/50 Correct", "Can you guess another one? (Type 'Exit' to quit)")

    if answer is None or answer.lower() == "exit":
        break

    answer = answer.strip().title()

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]

        label_turtle.goto(int(state_data.x.values[0]), int(state_data.y.values[0]))
        label_turtle.write(state_data.state.values[0])
        counter += 1

# Final score display
background_turtle.penup()
background_turtle.hideturtle()
background_turtle.goto(0, 0)
background_turtle.write(f"You scored {counter} out of {len(states)}",
                        align="center", font=("Arial", 20, "bold"))

# Save missed states to a CSV file
missed_states = [state for state in states if state not in guessed_states]
pandas.DataFrame(missed_states, columns=["Missed States"]).to_csv("missed_states.csv", index=False)

# Keeps the window open until clicked
screen.exitonclick()
