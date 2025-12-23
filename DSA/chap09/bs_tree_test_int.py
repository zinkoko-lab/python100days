# ２分探索木クラスBinarySearchTreeの利用例（データはint型のキーのみ）

from enum import Enum
from bs_tree import BinarySearchTree

Menu = Enum('Menu', ['挿入', '削除', '探索', 'ダンプ', 'キー範囲', '終了'])

def select_Menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()                       # ２分探索木を生成

while True:
    match menu := select_Menu():                # メニュー選択

     case Menu.挿入:                            # 挿入
        key = int(input('キー：'))
        if not tree.add(key, key):
            print('挿入失敗！')

     case Menu.削除:                            # 削除
        key = int(input('キー：'))
        tree.remove(key)

     case Menu.探索:                            # 探索
        key = int(input('キー：'))
        t = tree.search(key)
        if t is not None:
            print(f'そのキーをもつデータは存在します。')
        else:
            print('該当するデータはありません。')

     case Menu.ダンプ:                          # ダンプ
        tree.dump()

     case Menu.キー範囲:                        # キー範囲（最小値と最大値）
        print(f'キーの最小値＝{tree.min_key()}')
        print(f'キーの最大値＝{tree.max_key()}')

     case _:                                    # 終了
        break
