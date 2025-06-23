from PIL import Image

# 画像を開く
image = Image.open("blank_states_img.gif")

# サイズを取得（width, height の順）
width, height = image.size

print(f"幅: {width}px, 高さ: {height}px")
