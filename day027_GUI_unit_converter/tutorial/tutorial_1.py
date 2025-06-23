import tkinter as tk

# メインウィンドウを作成
window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")  # 横x縦

# ラベル（文字表示）
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()


# ボタン
def on_click():
    label.config(text="ボタンがクリックされました！")


button = tk.Button(window, text="クリックしてね", command=on_click)
button.pack()

# メインループ開始（これがないとウィンドウが表示されない）
window.mainloop()
