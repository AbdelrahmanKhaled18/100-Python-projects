import pandas as pd
from tkinter import *
import random
import os

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
PADDING = 50
FLIP_TIME = 3000

# Load data
current_card = {}
flip_timer = None

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


# Functions
def show_random_word():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(FLIP_TIME, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    show_random_word()


# Window setup
window = Tk()
window.title("Flashy")
window.config(padx=PADDING, pady=PADDING, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=show_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

# Start with first word
show_random_word()

window.mainloop()
