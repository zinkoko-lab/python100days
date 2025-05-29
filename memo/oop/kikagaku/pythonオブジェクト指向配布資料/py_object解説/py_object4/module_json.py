import json
menu = [
    {"name": "アイスコーヒー", "price": 200},
    {"name": "アイスカフェラテ", "price": 300},
    {"name": "アイスココア", "price": 350}
]

with open("menu.text", "w") as file:
    json.dump(menu, file, indent=3)