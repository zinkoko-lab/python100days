# 必要なモジュールをインポート
from random import choice
from os import system, name
from art import logo, vs
from game_data import data  # 人物やブランドのフォロワー情報を含むデータ


def clear_screen():
    """ターミナル画面をクリアする関数"""
    system("cls" if name == "nt" else "clear")  # Windowsならcls、それ以外ならclear


def two_rdm_data(prev_lst: list):
    """
    game_data.py のデータからランダムに2件を選びリストで返す関数。
    直前の結果があれば、1件を引き継ぎ、もう1件は新たに選ぶ。
    """
    idx_lst = list(range(len(data)))  # dataのインデックスのリストを作成
    next_lst = list()  # 次に使用するデータを格納するリスト

    if len(prev_lst) == 0:
        # ゲームの開始時はデータが無いため、ランダムに2件選ぶ
        for _ in range(2):
            tmp_idx = choice(idx_lst)
            idx_lst.remove(tmp_idx)  # 重複を避けるために選んだインデックスを除去
            next_lst.append(data[tmp_idx])
    else:
        # 一つ前のデータのうち「後ろの要素」を引き継ぎ、もう1件を新たに選ぶ
        next_lst.append(prev_lst[-1])  # 前回のBを今回のAに
        for i in range(2):
            tmp_idx = data.index(prev_lst[i])  # すでに使われたデータのインデックス
            idx_lst.remove(tmp_idx)  # 重複を避けるために除外
        next_lst.append(data[choice(idx_lst)])  # 新しいデータを追加（今回のB）

    return next_lst


def describe_data(who: dict):
    """
    引数として渡されたデータ（人物など）の内容を表示する関数
    """
    print(f"{who['name']}, ", end="")
    # print(f"{who['follower_count']}, ", end='')  # テスト用にフォロワー数も表示可能
    print(f"{who['description']}, ", end="")
    print(f"from {who['country']}.")


def check_answer(user_guess: str, a_follower: int, b_follower: int):
    """入力された結果に応じて正解かどうか判定する"""
    if user_guess == "a":
        return a_follower > b_follower
    elif user_guess == "b":
        return b_follower > b_follower
    else:
        return False  # 無効な入力時は不正解扱い


# --- メイン処理 ---
a_and_b = list()  # AとBのデータを保持するリスト
result = True  # ゲーム継続フラグ
score = 0  # スコアの初期化

while result:
    a_and_b = two_rdm_data(a_and_b)  # AとBのデータを取得
    data_a, data_b = a_and_b  # データの展開

    clear_screen()  # 画面をクリア
    print(logo)  # ロゴを表示

    if score > 0:
        print(f"You're right! Current score: {score}")  # 正解したときのスコア表示

    print(f"Compare A: ", end="")
    describe_data(data_a)  # Aの情報表示
    print(vs)
    print(f"Against B: ", end="")
    describe_data(data_b)  # Bの情報表示

    # ユーザーの選択を入力（小文字化・空白除去）
    guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

    # 入力結果に応じて正解かどうかを判定
    result = check_answer(guess, data_a["follower_count"], data_b["follower_count"])

    # 正解ならスコア加算
    if result:
        score += 1

# ゲーム終了後の表示
clear_screen()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
