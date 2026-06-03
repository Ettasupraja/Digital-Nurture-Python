import csv

employees = []

with open("employees.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

high_salary = [emp for emp in employees if emp["salary"] > 50000]

average = sum(emp["salary"] for emp in employees) / len(employees)

print("Employees > 50000:")
for emp in high_salary:
    print(emp)

print("Average Salary:", average)