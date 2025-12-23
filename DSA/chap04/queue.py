# 固定長キュークラス（collections.dequeを利用）

from typing import Any
from collections import deque

class Queue:
    """固定長キュークラス（collections.dequeを利用）"""

    def __init__(self, maxlen: int = 256) -> None:
        """初期化"""
        self.capacity = maxlen
        self.__que = deque([], maxlen)

    def __len__(self) -> int:
        """キューに積まれているデータ数を返す"""
        return len(self.__que)

    def is_empty(self) -> bool:
        """キューは空であるか"""
        return not self.__que

    def is_full(self) -> bool:
        """キューは満杯か"""
        return len(self.__que) == self.__que.maxlen

    def enque(self, value: Any) -> None:
        """キューにvalueをエンキュー"""
        self.__que.append(value)

    def deque(self) -> Any:
        """キューからデータをデキュー"""
        return self.__que.popleft()

    def peek(self) -> Any:
        """キューからデータをピーク（先頭データをのぞき見）"""
        return self.__que[0]

    def clear(self) -> None:
        """キューを空にする（全データの削除）"""
        self.__que.clear()

    def find(self, value: Any) -> Any:
        """キューからvalueを探して添字（見つからなければ-1）を返す"""
        try:
            return self.__que.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """キューに含まれるvalueの個数を返す"""
        return self.__que.count(value)

    def __contains__(self, value: Any) -> bool:
        """キューにvalueは含まれているか"""
        return self.count(value)

    def dump(self) -> int:
        """ダンプ（キュー内の全データを先頭→末尾の順に表示）"""
        print(*list(self.__que))
