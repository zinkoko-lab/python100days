with open("hello.text", "w") as f:
    f.write("こんにちは。\nお元気ですか？")

with open("hello.text", "r") as f:
    str_lines = f.readlines()

for str_line in str_lines:
    print(str_line.strip())
