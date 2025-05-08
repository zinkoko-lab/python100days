bidders = {}
while True:
    while True:
        name = input("What's your name?: ")
        bid = int(input("What's your bid?: "))
        bidders[name] = bid

        any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
        if any_other_bidders != "yes":
            break
    max_bid = 1
    winners = {}
    for key in bidders:
        if bidders[key] > max_bid:
            winners[key] = bidders[key]
        elif bidders[key] == max_bid:
            winners[key] = bidders[key]
        else:
            pass

    # cont number of winners　-> len(winners)
    # if number of winners is more than one -> winnersたちをもう一度入札させて
    # 最後にwinnerが一人になるまで
    # 例外処理を考える
    # UIを考える(最後に)


# print(bidders)

# import time
# print("Hello")
# time.sleep(3)
# print("\n" * 100)
# something = input("Please say something: ")
# print("\n" * 100)
# print(f"You said: {something}")
