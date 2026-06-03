import json

students = {
    "supraja": [80, 85, 90],
    "padmaja": [75, 88, 92]
}

def calculate_gpa(grades):
    return round(sum(grades) / len(grades), 2)

with open("grades.json", "w") as file:
    json.dump(students, file)

with open("grades.json", "r") as file:
    data = json.load(file)

for student, grades in data.items():
    print(student, "GPA:", calculate_gpa(grades))

class_average = sum(
    calculate_gpa(grades) for grades in data.values()
) / len(data)

print("Class Average:", round(class_average, 2))