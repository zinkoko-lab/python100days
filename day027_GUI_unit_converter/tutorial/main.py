import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(
    text="I Am a Label.",
    font=("Arial", 24, "bold"),
)
my_label.pack()
my_label["text"] = "a new text"
my_label.config(text="a new text")


# Button


def button_clicked():
    text = user_input.get()
    my_label.config(text=f"Your input: {text}")


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

user_input = tkinter.Entry(width=10)
user_input.pack()

window.mainloop()


# about arguments

# import turtle

# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.write("some text", move=True)

# screen.mainloop()
