import tkinter as tk
from tkinter import font

# Tkinterのウィンドウを作成（表示はしない）
root = tk.Tk()
root.withdraw()  # ウィンドウを表示しないようにする

# フォント一覧を取得し、ソートして表示
available_fonts = sorted(font.families())

# 出力
for f in available_fonts:
    print(f)

root.destroy()
