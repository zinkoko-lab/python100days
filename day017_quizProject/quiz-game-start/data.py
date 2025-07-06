import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
resoponse = requests.get(url="https://opentdb.com/api.php", params=parameters)
resoponse.raise_for_status()
data = resoponse.json()
question_data = data["results"]

# question_data = [
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "JavaScript derives from a later version of Java",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "RAM stands for Random Access Memory.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "The Windows ME operating system was released in the year 2000.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "A Mac is not a PC",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
# ]
