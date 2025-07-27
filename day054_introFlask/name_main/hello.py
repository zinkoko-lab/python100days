def say_hello():
    print("Hello!")


print(f"__name__ in hello.py: {__name__}")

if __name__ == "__main__":
    # この中の処理は「直接実行した時だけ」動く
    say_hello()
