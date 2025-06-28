# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
check_mark_text = ""


# ---------------------------- TIMER RESET ------------------------------- #
def resest_timer():
    window.after_cancel(timer)
    # time_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    title_label.config(text="Timer", fg=GREEN)
    # reset check_marks
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # count: minで受け取る -> sec に変換　-> count * 60
    # count_down(WORK_MIN * 60)
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        # If it's the 8th rep:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # If it's 2nd/4th/6th rep:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # If it's the 1st/3rd/5st/7th rep:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    # display -> "00:00"(min:sec)
    time_instance = f"{minutes}:0{seconds}" if seconds < 10 else f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time_instance)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global check_mark_text
        check_mark_text = "✔" * (reps // 2)
        check_mark.config(text=check_mark_text)


# ---------------------------- ファイルのパス取得 ------------------------------- #
# PyInstaller環境でもファイルを取得できるパスを返す
def get_resource_path(relative_path):
    try:
        # PyInstallerで実行されている場合
        base_path = sys._MEIPASS
    except AttributeError:
        # 開発環境の場合
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk
import sys
import os


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(
    text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 42, "normal")
)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato.png のパスを取得
image_data_path = get_resource_path("tomato.png")
tomato_image = tk.PhotoImage(file=image_data_path)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = tk.Button(
    text="Start",
    bg=YELLOW,
    fg="black",
    font=(FONT_NAME, 16),
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=start_timer,
)
start_button.grid(column=0, row=2)

check_mark = tk.Label(background=YELLOW, fg=GREEN)
check_mark.config(padx=0, pady=0)
check_mark.grid(column=1, row=3)

reset_button = tk.Button(
    text="Reset",
    bg=YELLOW,
    fg="black",
    font=(FONT_NAME, 16),
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=resest_timer,
)
reset_button.grid(column=2, row=2)


window.mainloop()
