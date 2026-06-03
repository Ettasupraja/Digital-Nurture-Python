class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee:", self.name)

emp1 = Employee("supraja")
emp2 = Employee("Subbareddy")
emp3 = Employee("padmaja")

emp1.display()
emp2.display()
emp3.display()