import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()

# Draw text, centered at (100, 50)
canvas.create_text(100, 50, text="Hello, Canvas!", font=("Arial", 16), fill="blue")

# Draw text with top-left corner at (20, 20)
canvas.create_text(
    20, 20, anchor=tk.NW, text="Top Left", font=("Helvetica", 12), fill="red"
)

root.mainloop()
