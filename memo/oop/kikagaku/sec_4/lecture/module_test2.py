from module1 import Player, print_message


class Hero(Player):
    def encourage(self):
        print(f"{self.name}がみんなを勇気づける。")


john = Player(1, "JOHN")
leo = Hero(30, "LEO")

print(john)
print(leo)

print_message()
# echo_message("test") # <- errorになる
