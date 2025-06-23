import turtle
import pandas as pd

# セットアップ
screen = turtle.Screen()
screen.setup(width=750, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

typer = turtle.Turtle()
typer.color("black")
typer.hideturtle()
typer.penup()


# データ読み込み
df = pd.read_csv("50_states.csv")
states = df["state"].to_list()
guessed_states = []
not_guessed_states = states.copy()
TOTAL_STATES = len(states)
correct_count = 0


def get_state_coords(state_name):
    row = df[df["state"] == state_name]
    corrd = (row["x"].item(), row["y"].item())
    return corrd


# メイン処理
while correct_count < TOTAL_STATES:
    prompt_title = (
        f"{correct_count}/50 States Correct" if correct_count > 0 else "Guess the State"
    )
    answer_state = (
        screen.textinput(
            title=prompt_title,
            prompt="What's another state's name?",
        )
    ).title()

    if not answer_state:
        continue  # 空入力やキャンセルに対応

    if answer_state == "Exit":
        break

    if answer_state in states:
        if answer_state not in guessed_states:
            typer.goto(get_state_coords(answer_state))
            typer.write(answer_state, align="center", font=("Arial", 10, "bold"))
            guessed_states.append(answer_state)
            not_guessed_states.remove(answer_state)
            correct_count += 1

if len(guessed_states) == TOTAL_STATES:
    typer.goto(0, 250)
    typer.color("green")
    typer.write(
        "🎉 Congratulations! 🎉\nYou guessed all 50 states!",
        align="center",
        font=("Courier", 22, "bold"),
    )
    screen.exitonclick()
else:
    # user_typed_exit  ->  states_to_learn.csv(states name cannot gussed)
    states_to_learn_dict = {"States to learn": not_guessed_states}
    states_to_learn = pd.DataFrame(states_to_learn_dict)
    states_to_learn.to_csv("states_to_learn.csv")
