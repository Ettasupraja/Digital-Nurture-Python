import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} - {self.name} - ₹{self.salary}"

employees = {
    "E101": {"name": "supraja", "salary": 50000},
    "E102": {"name": "padmaja", "salary": 60000}
}

with open("emps.json", "w") as file:
    json.dump(employees, file)

with open("emps.json", "r") as file:
    data = json.load(file)

for emp_id, details in data.items():
    emp = Employee(emp_id, details["name"], details["salary"])
    print(emp)