class User:
    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name

    # @property以外は使わないと思う
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "":
            self.__name = name
        else:
            raise TypeError("name の値は文字列である必要があります")

    @name.deleter
    def name(self):
        del self.__name


user1 = User()
user1.name = "鈴木"
print(user1.name)
del user1.name
print(user1.name)


"""
@propertyだけを使う
setterは使わない
"""

from datetime import datetime

dt = datetime.strptime("2022-01-07", "%Y-%m-%d")

print(dt.year)  # @property のおかげでdt.yearの参照ができる
# dt.year = 2021 # 元のdatetimeライブラリーのdatetime classにはsetterを定義してないためエラーとなる
# 自分でclassを定義するときは慣習としてsetterは設定しない


# 下記のコードは @property デコレーターを使用しない getter/setter関数の定義の例
# class User:
#     def __init__(self, name=None):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         if isinstance(name, str) and name != "":
#             self.__name = name
#         else:
#             raise TypeError("name の値は文字列である必要があります")


# user1 = User()
# user1.set_name(1)
# print(user1.get_name())
