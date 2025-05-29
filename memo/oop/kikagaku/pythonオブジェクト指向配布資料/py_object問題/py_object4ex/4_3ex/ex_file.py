with open("hello.text", "w") as hello:
    hello.write("こんにちは。\nお元気ですか？")

with open("hello.text", "r") as hello:
    print(hello.read())