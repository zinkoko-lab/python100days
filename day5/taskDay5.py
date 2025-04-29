student_scores = [180, 124, 165, 173, 189, 169, 146]
max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"max_score = {max_score}")