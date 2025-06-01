import datetime

# print(datetime.date.today())  # 今日の日付を取得
# print(datetime.datetime.now())  # 現在の日付と時刻を取得

# お正月、クリスマスなど特定の日までの日数を簡単に求めることができます。
# 指定した年月日のdateオブジェクトを作成
# datetime.date(年,月,日)

# 2025年のクリスマス
xmas_2025 = datetime.date(2025, 12, 25)

# 日付Aから日付Bまでの日数を求める
# 日付B(dateオブジェクト) - 日付A(dateオブジェクト)
# 今日の日付
today = datetime.date.today()

# クリスマスまでの日数
before_xmas = xmas_2025 - today

# .daysを使って整数値の日数だけ取り出す
print(f"今年のクリスマスまで{before_xmas.days}日です。")

# ✅ ポイント
# timedelta は .days, .seconds, .total_seconds() などのプロパティを持っています。
# .days を使うと整数値だけ抜き出せるので、表示をシンプルにできます！
