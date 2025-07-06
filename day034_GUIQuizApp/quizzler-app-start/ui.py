from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_LABEL_FONT = ("Courier", 24, "normal")
QUESTION_TEXT_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            fg="white",
            font=SCORE_LABEL_FONT,
        )
        self.score_label.grid(row=0, column=1)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text That Is Very Long To Test Auto Wrapping",
            fill="black",
            font=QUESTION_TEXT_FONT,
            width=280,  # <--- 自動改行のための幅指定
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        self.check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.check_image,
            highlightthickness=0,
            bd=0,
            command=self.click_true_button,
        )
        self.true_button.grid(row=2, column=0)

        # False Button
        self.cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.cross_image,
            highlightthickness=0,
            bd=0,
            command=self.click_false_button,
        )
        self.false_button.grid(row=2, column=1)

        # generate the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_question)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            # ここで即 messagebox を呼ばず、after を使って Tkinter に再描画タイミングを与える
            self.window.after(
                1000, self.show_final_message  # 100ms 後に messagebox を呼ぶ
            )

    def show_final_message(self):
        messagebox.showinfo(
            title="Complete",
            message=f"You've completed the quiz.\nYour final score is: {self.quiz.score}/{len(self.quiz.question_list)}",
        )
        self.window.quit()

    def update_score(self):
        current_score = self.quiz.score
        self.score_label.config(text=f"Score: {current_score}")

    def click_true_button(self):
        is_right = self.quiz.check_answer(user_answer="true")
        self.give_feedback(is_right=is_right)

    def click_false_button(self):
        is_right = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_right=is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.update_score)
        self.window.after(1000, func=self.get_next_question)


if __name__ == "__main__":
    QuizInterface()
