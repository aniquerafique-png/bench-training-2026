students = [
    {"name": "Ali", "scores": [85, 78, 92], "subject": "Math"},
    {"name": "Sara", "scores": [90, 88, 95], "subject": "Physics"},
    {"name": "Ahmed", "scores": [70, 75, 72], "subject": "Chemistry"},
    {"name": "Fatima", "scores": [95, 91, 93], "subject": "Biology"},
    {"name": "Hassan", "scores": [80, 82, 79], "subject": "English"}
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def class_topper(students):
    topper = None
    highest_avg = -1
    
    for student in students:
        avg = calculate_average(student["scores"])
        if avg > highest_avg:
            highest_avg = avg
            topper = student
            
    return topper

topper = class_topper(students)
topper_name = topper["name"]

sorted_students = sorted(
    students,
    key=lambda s: calculate_average(s["scores"]),
    reverse=True
)

print("Student Report")
print("-" * 40)

for student in sorted_students:
    avg = calculate_average(student["scores"])
    grade = get_grade(avg)

    line = f"{student['name']} | {avg:.2f} | {grade}"

    if student["name"] == topper_name:
        line += " *** TOP ***"

    print(line)