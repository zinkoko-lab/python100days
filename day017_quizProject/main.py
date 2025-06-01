class User:
    """
    ユーザー同士のフォロー・アンフォロー機能を持つUserクラス
    """

    def __init__(self, id, name):
        """
        ユーザーIDと名前を設定し、フォロワー・フォロー中のリストを初期化
        """
        self._id = id
        self._name = name
        self.__followers = []  # フォロワーリスト
        self.__followings = []  # フォロー中のリスト
        self.__follower_cnt = 0  # フォロワー数
        self.__following_cnt = 0  # フォロー中の数

    def follow(self, user):
        """
        指定したユーザーをフォローする
        """
        if self != user and self not in user.__followers:
            user.__followers.append(self)
            user.__follower_cnt += 1
            self.__followings.append(user)
            self.__following_cnt += 1
            print(f"{self._name} が {user._name} をフォローしました。")

    def unfollow(self, user):
        """
        指定したユーザーのフォローを外す
        """
        if user in self.__followings:
            self.__followings.remove(user)
            self.__following_cnt -= 1
            user.__followers.remove(self)
            user.__follower_cnt -= 1
            print(f"{self._name} が {user._name} のフォローを外しました。")

    def get_followers(self):
        """
        フォロワーリストを表示
        """
        print(f"=== {self._name} のフォロワー（{self.__follower_cnt} 人） ===")
        if self.__follower_cnt == 0:
            print("フォロワーはいません。")
        else:
            for follower in self.__followers:
                print(f"・{follower._name}")
        print()

    def get_followings(self):
        """
        フォロー中リストを表示
        """
        print(f"=== {self._name} がフォロー中（{self.__following_cnt} 人） ===")
        if self.__following_cnt == 0:
            print("フォロー中のユーザーはいません。")
        else:
            for following in self.__followings:
                print(f"・{following._name}")
        print()

    def get_follower_count(self):
        """
        フォロワー数を返す
        """
        return self.__follower_cnt

    def get_following_count(self):
        """
        フォロー中の数を返す
        """
        return self.__following_cnt


# =======================
# テストコード
# =======================
user_1 = User(1, "user1")
user_2 = User(2, "user2")
user_3 = User(3, "user3")
user_4 = User(4, "user4")
user_5 = User(5, "user5")

# user_1をフォロー
user_2.follow(user_1)
user_3.follow(user_1)
user_4.follow(user_1)
user_5.follow(user_1)

# 結果表示
user_1.get_followers()
user_2.get_followers()
user_1.get_followings()
user_2.get_followings()

# アンフォロー
user_2.unfollow(user_1)
user_1.get_followers()
user_2.get_followings()
