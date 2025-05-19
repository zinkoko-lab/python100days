import random

def coin_toss():
    random_int = random.randint(0, 1)
    if random_int == 1:
        return "Head"
    else:
        return "Tail"

numberOf_toss = 100000
NT = numberOf_toss
countHead = 0
countTail = 0

while numberOf_toss > 0:
    result = coin_toss()
    if result == 'Head':
        countHead += 1
    else:
        countTail += 1
    numberOf_toss -= 1

probHead = (countHead / NT) * 100
probTail = (countTail / NT) * 100

print(f"P(Head) = {probHead}")
print(f"P(Tail) = {probTail}")

# import my_module
# rdn_int = random.randint(1, 10)
# print(rdn_int)
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)