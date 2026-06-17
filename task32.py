students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 94]},
    {"name": "Charlie", "grades":}
]
print("Student Grade Averages:")
print("-" * 25)
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"Name: {name} | Average: {average:.2f}")