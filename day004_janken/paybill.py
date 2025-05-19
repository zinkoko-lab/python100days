import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))

# 2nd Option
numFri = len(friends)
upperLmt = numFri - 1
rdmIdx = random.randint(0, upperLmt)

whoPay = friends[rdmIdx]
print(whoPay)