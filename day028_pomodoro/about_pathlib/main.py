from pathlib import Path

# あるディレクトリのパスを取得する
# path = Path("/Users/zinkoko/projects/python100days/day028_pomodoro")

# ディレクトリ下のパスオブジェクトもfor文で取り出すことが可能
# dir_g = path.iterdir()
# for x in dir_g:
#     print(x)

# ディレクトリ下のパスオブジェクトもリストでまとめることも可能
# print(list(path.iterdir()))

# 現在いるディレクトリのPathオブジェクトを取得する
cwd_path = Path.cwd()
dir1 = cwd_path / "dir1"

dir1_g = dir1.iterdir()
for x in dir1_g:

    # print(x) <- path object が出される
    # print(type(x)) # <class 'pathlib._local.PosixPath'>

    # 文字列で取り出したいときはstr()関数を使う
    print(str(x))

    # ファイル名、フォルダ名を取得
    print(x.name)
    print(type(x.name))
