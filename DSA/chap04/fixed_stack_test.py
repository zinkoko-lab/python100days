# 固定長スタッククラスFixedStackの利用例

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['プッシュ', 'ポップ', 'ピーク', '探索', 'ダンプ', '終了'])

def select_menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)      # 最大64個プッシュできるスタック

while True:
    print(f'現在のデータ数：{len(s)} / {s.capacity}')

    match menu := select_menu():                # メニュー選択

     case Menu.プッシュ:                        # プッシュ
        x = int(input('データ：'))
        try:
            s.push(x)
        except FixedStack.Full:
            print('スタックが満杯です。')

     case Menu.ポップ:                          # ポップ
        try:
            x = s.pop()
            print(f'ポップしたデータは{x}です。')
        except FixedStack.Empty:
            print('スタックが空です。')

     case Menu.ピーク:                          # ピーク
        try:
            x = s.peek()
            print(f'ピークしたデータは{x}です。')
        except FixedStack.Empty:
            print('スタックが空です。')

     case Menu.探索:                            # 探索
        x = int(input('値：'))
        if x in s:
            print(f'{s.count(x)}個含まれ先頭の位置は{s.find(x)}です。')
        else:
            print('その値は含まれません。')

     case Menu.ダンプ:                          # ダンプ
        s.dump()

     case _:
          break
