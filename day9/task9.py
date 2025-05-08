# エラー処理
# y = 1
# while True:
#     try:
#         x = int(input("数字を入力してください: "))
#         z = y / x
#         break
#     except ValueError:
#         print("あらら！これは有効な数字ではありません。どうぞもう一度。")

# exercise

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# def convert_grade(score: int):
#     if score >= 91:
#         return "Outstanding"
#     elif score >= 81:
#         return "Exceeds Expectations"
#     elif score >= 71:
#         return "Acceptable"
#     else:
#         return "Fail"

# for key in student_scores:
#     score = student_scores[key]
#     grade = convert_grade(score)
#     student_grades[key] = grade

# print(student_grades)

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# Print Lille from travel_log
# print(travel_log["France"][1])

# Nested list
# nested_list = ["A", "B", ["C", "D"]]

# Print "D" from nested_list
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg","Stuttgart"],
        "total_visits": 5
    }
}

# Print "Stuttgart" from travel_log
print(travel_log["Germany"]["cities_visited"][2])
