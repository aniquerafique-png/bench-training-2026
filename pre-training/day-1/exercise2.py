def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"


scores = [45, 72, 91, 60, 38, 85]

for score in scores:
    result = grade_classifier(score)
    print(f"Score: {score} -> {result}")