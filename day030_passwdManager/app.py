from random import randint, choice, shuffle
from characters import letters, numbers, symbols
import sys, os
import tkinter as tk
from tkinter import messagebox
import pyperclip
import json
from pathlib import Path


# ---------------------------- GET FILE PATH(logo_image) ------------------------------- #
# PyInstaller環境でもファイルを取得できるパスを返す
def get_resource_path(relative_path):
    try:
        # PyInstallerで実行されている場合
        base_path = sys._MEIPASS
    except AttributeError:
        # 開発環境の場合
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


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


# ---------------------------- Get Json Data Path ------------------------------- #
def get_user_data_path(filename="data.json"):
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller app化後の環境
        user_dir = Path.home() / "Documents" / "MyAppData"
    else:
        # 開発環境
        user_dir = Path.cwd()

    user_dir.mkdir(parents=True, exist_ok=True)
    return user_dir / filename


json_data_path = get_user_data_path()
print(f"Using data path: {json_data_path}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get().lower()
    id = email_entry.get()
    passwd = passwd_entry.get()
    new_data = {website: {"email": id, "password": passwd}}

    if len(website) < 1 or len(passwd) < 1:
        messagebox.showwarning(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            message=f"These are the details you entered:\nEmail: {id}\nPassword:{passwd}\nIs it ok to save?",
        )
        if is_ok:
            try:
                with open(file=json_data_path, mode="r") as f:
                    # Reading old data
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                # ファイルがない・空である場合、新規作成して new_data を書き込み
                with open(file=json_data_path, mode="w") as f:
                    json.dump(new_data, f, indent=4)
                # オーナーだけ読み書き可能
                os.chmod(json_data_path, 0o600)
            else:
                if website in data:
                    is_ok = messagebox.askokcancel(
                        message=f"details for {website} already exits.\nDo you overwrite on the existing data?"
                    )
                if is_ok:
                    # Updating old data with new data
                    data.update(new_data)
                    # 正常に読み込めた場合は更新した data を書き込み
                    with open(file=json_data_path, mode="w") as f:
                        json.dump(data, f, indent=4)
            finally:
                web_entry.delete(0, tk.END)
                passwd_entry.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_passwd():
    website = web_entry.get().lower()
    if len(website) > 0:
        try:
            with open(file=json_data_path, mode="r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showwarning(message="No Data File Found.")
        else:
            try:
                email = data[website]["email"]
                password = data[website]["password"]
            except KeyError:
                messagebox.showwarning(message=f"No details for {website} exits.")
            else:
                messagebox.showinfo(
                    title=website, message=f"email: {email}\npassword: {password}"
                )


# ---------------------------- GET FILE PATH ------------------------------- #
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
web_entry = tk.Entry(width=21)
web_entry.focus()
web_entry.grid(row=1, column=1, sticky="w")

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

search_btn = tk.Button(
    text="Search",
    width="13",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=find_passwd,
)
search_btn.grid(row=1, column=2)


window.mainloop()
