# tkinterライブラリをtkとしてインポート
import tkinter as tk


# マイルをキロメートルに変換する関数（1マイル = 1.609km）
def mile_to_km(mile: float):
    return round(mile * 1.609, 2)  # 小数点以下2桁に丸める


# 「Calculate」ボタンがクリックされたときの処理
def convert_mile_to_km():
    try:
        # 入力された文字列をfloat型に変換
        input_mile = float(user_input.get())
        # マイルをキロに変換して結果ラベルに表示
        km = mile_to_km(input_mile)
        result_label.config(text=str(km))
    except ValueError:
        # 数値以外の入力があった場合のエラー処理
        result_label.config(text="Invalid input")  # 無効な入力と表示


# メインウィンドウの作成
window = tk.Tk()
window.title("Mile to Km Converter")  # ウィンドウのタイトル
window.config(padx=20, pady=20)  # ウィンドウの余白（上下左右）

# ユーザー入力用のEntry（入力欄）
user_input = tk.Entry(width=7)
user_input.insert(tk.END, "0")  # 初期値を0に設定
user_input.grid(column=1, row=0)  # グリッドの位置を指定

# 「Miles」という単位のラベル
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

# 「is equal to」というテキストラベル
equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

# 結果を表示するラベル（初期値は0）
result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

# 「Km」という単位のラベル
km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

# 計算を実行するボタン
button = tk.Button(text="Calculate", command=convert_mile_to_km)
button.grid(column=1, row=2)

# ウィンドウを表示してイベントループを開始
window.mainloop()
