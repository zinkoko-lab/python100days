import tkinter as tk
from tkinter import messagebox
import sys
import os
import pandas as pd
from random import choice

# ---------------------------- CONFIG ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FLIP_DELAY_MS = 3000


# ---------------------------- PATH UTIL ------------------------------- #
def get_resource_path(relative_path):
    """Return the path for bundled PyInstaller or local environment."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------------------- LOAD WORDS ------------------------------- #
learn_words_path = get_resource_path("data/words_to_learn.csv")
french_words_path = get_resource_path("data/french_words.csv")

try:
    words_df = pd.read_csv(learn_words_path)
except (FileNotFoundError, pd.errors.EmptyDataError):
    words_df = pd.read_csv(french_words_path)

words_list = words_df.to_dict(orient="records")
current_card = {}


# ---------------------------- CARD ACTIONS ------------------------------- #
def show_new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    if not words_list:
        messagebox.showinfo(
            title="Complete", message="すべて覚えました！おめでとうございます！"
        )
        window.quit()
        return

    current_card = choice(words_list)
    canvas.itemconfig(card_background_img, image=card_front_img)
    canvas.itemconfig(card_title_text, text="French", fill="black")
    canvas.itemconfig(card_word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(FLIP_DELAY_MS, flip_card)


def flip_card():
    canvas.itemconfig(card_background_img, image=card_back_img)
    canvas.itemconfig(card_title_text, text="English", fill="white")
    canvas.itemconfig(card_word_text, text=current_card["English"], fill="white")


def mark_as_known():
    words_list[:] = [
        word for word in words_list if word["French"] != current_card["French"]
    ]
    pd.DataFrame(words_list).to_csv(learn_words_path, index=False)
    show_new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("French Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(FLIP_DELAY_MS, flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file=get_resource_path("images/card_front.png"))
card_back_img = tk.PhotoImage(file=get_resource_path("images/card_back.png"))
card_background_img = canvas.create_image(400, 263, image=card_front_img)

card_title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button
wrong_img = tk.PhotoImage(file=get_resource_path("images/wrong.png"))
wrong_button = tk.Button(
    image=wrong_img, highlightthickness=0, borderwidth=0, command=show_new_card
)
wrong_button.grid(row=1, column=0)

# Right Button
right_img = tk.PhotoImage(file=get_resource_path("images/right.png"))
right_button = tk.Button(
    image=right_img, highlightthickness=0, borderwidth=0, command=mark_as_known
)
right_button.grid(row=1, column=1)

show_new_card()
window.mainloop()
