class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # checking if we're the end of the quiz
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    # checking if the answer was correct
    def check_answer(self, answer, correct_answer):
        if answer.lower().strip() == correct_answer.lower().strip():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}\n")

    # asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )
        self.check_answer(user_answer, current_question.answer)
