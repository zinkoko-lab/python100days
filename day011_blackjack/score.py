# write a function to calculate the score                                                                   │
cards = [2, 2, 2, 11, 2, 11, 11]

# if hands contain any ACE(11):
# 1 -> 11 = 12 - 1
# 2 -> 10 = 12 - 2
# # 3 -> 9 = 12 - 3
# # N -> 12 - N
# ACE 1 card:
# if hands have one ACE card and sum of another cards < 11 : ace = 11
# if hands have one ACE card and sum of another cards => 11 : ace = 1

# ACE 2 cards:
# if hands have two cards and sum of another cards < 10 : ace = 11, ace = 1
# if hands have two cards and sum of another cards >= 10 : ace = 1, 1

# ACE N cards and more:
# if hands have N cards and sum of another cards < (12 - N) : ace = 11, ace = 1
# if hands have N cards and sum of another cards >= (12 - N) : ace = 1, 1

# if 11 in cards:
#     ace_cnt = cards.count(11)
#     std_score = 12 - ace_cnt
#     # sum of cards except ace:
#     tmp_score = sum([x for x in cards if x != 11])
#     tmp_cards = []
#     if tmp_score >= std_score:
#         for card in cards:
#             if card == 11:
#                 tmp_cards.append(1)
#             else:
#                 tmp_cards.append(card)

#     else:
#         idx_of_fst_ace = cards.index(11)
#         for idx in range(len(cards)):
#             if idx != idx_of_fst_ace:
#                 if cards[idx] == 11:
#                     tmp_cards.append(1)
#                 else:
#                     tmp_cards.append(cards[idx])
#             else:
#                 tmp_cards.append(cards[idx])

# else:
#     tmp_cards = cards


# score = sum(tmp_cards)

# print(f"cards: {cards}")
# print(f"tmp_cards: {tmp_cards}")
# print(f"score: {score}")

def calc_score(cards: list):
    dummy_lst = []
    ace = 11
    alt_ace = 1
    magic_number = 12
    if ace in cards:
        ace_cnt = cards.count(ace)
        score_lmt = magic_number - ace_cnt
        score_without_ace = sum([_ for _ in cards if _ != ace])
        if score_without_ace >= score_lmt:
            for card in cards:
                if card == ace:
                    dummy_lst.append(alt_ace)
                else:
                    dummy_lst.append(card)
        else:
            first_ace_idx = cards.index(ace)
            for idx in range(len(cards)):
                if idx != first_ace_idx:
                    if cards[idx] == ace:
                        dummy_lst.append(alt_ace)
                    else:
                        dummy_lst.append(cards[idx])
                else:
                    dummy_lst.append(cards[idx])
    else:
        dummy_lst = cards

    return sum(dummy_lst)

cards = [8, 8, 11, 11]

score = calc_score(cards=cards)

print(score) # ans : 17
