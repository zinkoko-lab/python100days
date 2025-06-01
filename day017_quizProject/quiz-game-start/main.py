from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from clear import clear_screen
from html import unescape

question_bank = []
for q in question_data:
    question = unescape(q["question"])
    correct_answer = unescape(q["correct_answer"])
    question_bank.append(Question(question, correct_answer))

quiz = QuizBrain(question_bank)

clear_screen()
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
