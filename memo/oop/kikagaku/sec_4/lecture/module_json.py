import json

menu = [
    {"name": "アイスコーヒー", "price": 200},
    {"name": "アイスカフェラテ", "price": 300},
    {"name": "アイスココア", "price": 350},
]

with open("menu.txt", "w") as f:
    json.dump(menu, f, indent=3)
    # json.dump(menu, f, indent=3, ensure_ascii=False)
