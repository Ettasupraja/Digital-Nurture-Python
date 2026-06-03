def merge_employee_data():
    emp1 = {"name": "Supraja", "salary": 75000}
    emp2 = {"department": "IT"}

    emp1.update(emp2)

    print(emp1)

merge_employee_data()