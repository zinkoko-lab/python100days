import module1 as m


class Hero(m.Player):
    def encourage(self):
        print(f"{self.name}がみんなを勇気づける。")


john = m.Player(1, "JOHN")
leo = Hero(30, "LEO")

print(john)
print(leo)

m.print_message()
m.echo_message("test")
