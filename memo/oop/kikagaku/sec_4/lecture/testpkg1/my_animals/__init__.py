# __init__.py

from .dog import bark
from .cat import meow
from .bird import tweet

__all__ = [
    "bark",
    "meow",
    "tweet",
]  # import * したときに読み込まれるシンボルを指定（任意）
