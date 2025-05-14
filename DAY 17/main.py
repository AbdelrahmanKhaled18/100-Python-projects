from question_model import QuestionModel
from data import question_data
import random

from quiz_brain import QuizBrain

question_bank = [QuestionModel(item["text"], item["answer"]) for item in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
