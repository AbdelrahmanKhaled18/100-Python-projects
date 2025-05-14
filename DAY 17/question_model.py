class QuestionModel:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.answer}"