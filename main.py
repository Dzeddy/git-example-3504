# Student Grades Processing Program with Logic Errors

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 67},
    {"name": "David", "score": 73},
    {"name": "Eva", "score": 58},
    {"name": "Frank", "score": 90},
    {"name": "Grace", "score": 77},
    {"name": "Hannah", "score": 88},
    {"name": "Ian", "score": 95},
    {"name": "Jane", "score": 81},
]

grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
total_score = 0

for student in students:
    score = student["score"]
    total_score += score

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    grade_counts[grade] += 1
    student["grade"] = grade

average_score = total_score / len(students)

print("Grade Summary:")
for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count} students")

print(f"\nAverage Score: {average_score:.2f}")

# Optional: Print student grades
print("\nStudent Grades:")
for student in students:
    print(f"{student['name']}: {student['grade']}")
