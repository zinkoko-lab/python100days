import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# データを格納する辞書
us_states_coor = {"state": [], "x": [], "y": []}


def get_coor_us_states(x, y):
    print("Click on the state you typed!")
    state_name = input("Tell me state name: ").title()  # 頭文字を大文字に

    us_states_coor["state"].append(state_name)
    us_states_coor["x"].append(x)
    us_states_coor["y"].append(y)

    print(f"Successfully appended! ({len(us_states_coor['state'])}/50)")

    if len(us_states_coor["state"]) >= 50:
        print("50 states collected. Saving to CSV and stopping.")
        df = pd.DataFrame(us_states_coor)
        df.to_csv("us_states_coor.csv", index=False)  # CSVファイルに保存
        turtle.onscreenclick(None)  # クリック無効化


turtle.onscreenclick(get_coor_us_states)
turtle.mainloop()
