import module1


class Hero(module1.Player):
    def encourage(self):
        print(f"{self.name}がみんなを勇気づける。")


john = module1.Player(1, "JOHN")
leo = Hero(30, "LEO")

print(john)
print(leo)

module1.print_message()
module1.echo_message("test")
