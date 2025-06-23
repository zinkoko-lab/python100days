import tkinter as tk


def show_text():
    user_input = entry.get()
    label.config(text=f"入力された内容：{user_input}")


window = tk.Tk()
window.title("Entry Example")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="表示", command=show_text)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()
