from tkinter import Tk, Label, Canvas, Button, PhotoImage

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            self.window,
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Keep references to the images
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            self.window,
            image=self.true_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.truePressed
        )
        self.false_button = Button(
            self.window,
            image=self.false_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.falsePressed
        )

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def truePressed(self):
        self.giveFeedback(self.quiz.check_answer("True"))

    def falsePressed(self):
        self.giveFeedback(self.quiz.check_answer("False"))

    def giveFeedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.getNextQuestion)
