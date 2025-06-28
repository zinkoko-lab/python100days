from random import randint, choice, shuffle
from characters import letters, numbers, symbols
import sys, os
import tkinter as tk
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwd_gen():
    num_letters = randint(8, 10)
    num_nums = randint(2, 4)
    num_symbols = randint(2, 4)

    password = [choice(letters) for _ in range(num_letters)]
    password += [choice(numbers) for _ in range(num_nums)]
    password += [choice(symbols) for _ in range(num_symbols)]

    shuffle(password)
    password = "".join(password)
    passwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    id = email_entry.get()
    passwd = passwd_entry.get()

    if len(website) < 1 or len(passwd) < 1:
        messagebox.showwarning(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            message=f"These are the details you entered:\nEmail: {id}\nPassword:{passwd}\nIs it ok to save?",
        )
        if is_ok:
            with open(file="data.txt", mode="a") as f:
                f.write(f"{website} | {id} | {passwd}\n")
                web_entry.delete(0, tk.END)
                passwd_entry.delete(0, tk.END)


# ---------------------------- GET IMAGE FILE PATH ------------------------------- #
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


window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
image_data_path = get_resource_path("logo.png")
logo_image = tk.PhotoImage(file=image_data_path)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

# labels
website_label = tk.Label(text="Website:", width=11, anchor="e")
website_label.grid(row=1, column=0, padx=1)

name_label = tk.Label(text="Email/Username:", width=11, anchor="e")
name_label.grid(row=2, column=0, padx=1)

passwd_label = tk.Label(text="Password:", width=11, anchor="e")
passwd_label.grid(row=3, column=0, padx=1)


# entry
web_entry = tk.Entry(width=39)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_entry = tk.Entry(width=39)
email_entry.insert(0, "example@abcmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

passwd_entry = tk.Entry(width=21)
passwd_entry.grid(row=3, column=1, sticky="w")

# buttons
pwd_gen_btn = tk.Button(
    text="Generate Password",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=passwd_gen,
)
pwd_gen_btn.grid(row=3, column=2)

add_btn = tk.Button(
    text="Add",
    width=36,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=save,
)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
