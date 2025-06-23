import tkinter as tk
import pandas as pd

# データ読み込み
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def convert():
    word = entry.get().upper()
    result = [nato_dict[char] for char in word if char.isalpha()]
    if result:
        output_label.config(text=" ".join(result))
    else:
        output_label.config(text="無効な文字が含まれています")


# GUI作成
window = tk.Tk()
window.title("NATO Phonetic Converter")
window.geometry("400x200")

tk.Label(window, text="英単語を入力してください").pack()
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="変換", command=convert).pack()
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
