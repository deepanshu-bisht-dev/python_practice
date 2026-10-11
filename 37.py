# Student Result
def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    return "F"


students = {
    "Rahul": [78, 85, 90],
    "Amit": [60, 70, 65],
    "Priya": [92, 88, 95],
    "Neha": [35, 40, 30],
    "Karan": [55, 62, 48],
}

topper = None
topper_pct = -1

for name, marks in students.items():
    total = sum(marks)
    pct = total / len(marks)          # 3 subjects, har ka max 100 maan ke
    grade = get_grade(pct)
    print(f"{name}: Total = {total}, Percentage = {pct:.2f}%, Grade = {grade}")
    if pct > topper_pct:
        topper_pct = pct
        topper = name

print(f"Topper: {topper} ({topper_pct:.2f}%)")