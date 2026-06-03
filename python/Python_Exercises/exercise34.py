def get_salary(department, employee):
    employees = {
        "IT": {
            "John": 50000,
            "David": 60000
        },
        "HR": {
            "Sara": 45000
        }
    }

    if department in employees:
        if employee in employees[department]:
            print("Salary:", employees[department][employee])
        else:
            print("Employee not found")
    else:
        print("Department not found")

get_salary("IT", "John")