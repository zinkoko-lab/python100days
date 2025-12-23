# n個の記号文字*をw個ごとに改行しながら表示（その３）

print('記号文字*を表示します。')
n = int(input('全部で何個：'))
w = int(input('何個ごとに改行：'))

print(n // w * (w * '*' + '\n'), end = r * '*' + '\n' if (r := n % w) else '')
