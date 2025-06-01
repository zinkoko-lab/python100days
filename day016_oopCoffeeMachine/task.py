from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table.align)

print(table)

table.align = "l"
print(table)

table.align = "r"
print(table)

table.valign = "t"
print(table)
