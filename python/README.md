# Cognizant-Python
### EX-01:Simple Hello World
### Code:
```
print("Hello World!")
```
### output:
<img width="1162" height="103" alt="image" src="https://github.com/user-attachments/assets/88b0da39-83f0-4282-9030-877b730f5c04" />

### EX-02:Jupyter Notebook

### Code:
```
print("Hello from Jupyter!")
```
### output
<img width="738" height="298" alt="image" src="https://github.com/user-attachments/assets/594bc21c-01de-448f-9241-49b413efe979" />

### EX-03:VS Code Setup
### code:
```
print("Hello, Python in VS Code!")
```

### output:

<img width="1155" height="104" alt="image" src="https://github.com/user-attachments/assets/bdcd4e52-705b-42e9-9f39-ef200c733b89" />

### EX-04:Float Precisiona
### code:
```
def calculate_net_salary(salary, tax_rate):

    if salary <= 0:
        print("Invalid Salary")
        return

    if tax_rate < 0 or tax_rate > 1:
        print("Invalid Tax Rate")
        return

    tax = salary * tax_rate
    net_salary = salary - tax

    print(f"Net Salary: {net_salary:.2f}")


salary = 75000.5
tax_rate = 0.18

calculate_net_salary(salary, tax_rate)
```
### output:
<img width="1152" height="110" alt="image" src="https://github.com/user-attachments/assets/8dcfaf57-8a5b-4987-95cf-11bf4aedeaa0" />

### EX-05:Multiple Assignment
## code:
```
def display_coordinates(coords):

    if len(coords) != 2:
        print("Invalid Coordinates")
        return

    x, y = coords

    print("X =", x)
    print("Y =", y)

coordinates = (10, 20)

display_coordinates(coordinates)
```
### output:
<img width="1141" height="120" alt="image" src="https://github.com/user-attachments/assets/34dd5dcc-741e-46a9-a3a0-04bc8aefe007" />

### EX-06:Modulo Operator
## code:
```
def check_even_odd(number):
    if not isinstance(number, int):
        return "Invalid Number"

    return "Even" if number % 2 == 0 else "Odd"

number = 17
print(check_even_odd(number))

```
output:
<img width="1141" height="120" alt="image" src="https://github.com/user-attachments/assets/95e5683d-d271-477c-a54b-6f1fc7df9b40" />

### EX-07:Floor Division
### code:
```
def split_bill(total_bill, people):
    if total_bill <= 0 or people <= 0:
        return "Invalid Input"

    share = total_bill // people
    return f"Each person pays: {share}"

print(split_bill(1250, 4))
```
### output:
<img width="631" height="79" alt="image" src="https://github.com/user-attachments/assets/c4c34217-f3f7-4579-9069-c376a8417bb3" />

### EX-08:Min/Max Functions
### code:
```
def salary_stats(salaries):
    if not salaries:
        return "Empty List"

    return f"Highest: {max(salaries)}, Lowest: {min(salaries)}"

salaries = [50000, 75000, 62000, 95000]

print(salary_stats(salaries))
```
### output:
<img width="631" height="93" alt="image" src="https://github.com/user-attachments/assets/2487f984-b66b-4964-8bc8-7795e0f5330f" />

### EX-09:Basic Input
### code:
```
def greet_user():

    name = input("Enter your name: ")

    if name.strip() == "":
        print("Name cannot be empty")
        return

    print("Hello,", name)


greet_user()
```
### output:
<img width="613" height="110" alt="image" src="https://github.com/user-attachments/assets/b11f7ea3-f1ec-4fe6-bc0f-f67e17642f64" />

### EX-10:Numeric Input
### code:
```
def next_year_age():
    age = input("Enter your age: ")

    if not age.isdigit():
        print("Invalid age")
        return

    age = int(age)
    print(f"Next year you'll be {age + 1}")

next_year_age()
```
### output:
<img width="646" height="99" alt="image" src="https://github.com/user-attachments/assets/99b7dfe2-87e2-4026-ac32-ca604f3c17a8" />

### EX-11:Float Input
### code
```
def kg_to_lbs():
    try:
        kg = float(input("Enter weight in kg: "))

        if kg <= 0:
            print("Invalid weight")
            return

        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs:.2f}")

    except ValueError:
        print("Invalid input")

kg_to_lbs()
```
### output:
<img width="625" height="98" alt="image" src="https://github.com/user-attachments/assets/8b05871f-4f5f-4a40-a0eb-10450d9e9249" />

### EX-12:Simple If
### code:
```
def check_pass(marks):
    if marks < 0 or marks > 100:
        print("Invalid Marks")
        return

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

marks = 75
check_pass(marks)

```
### output:
<img width="650" height="94" alt="image" src="https://github.com/user-attachments/assets/191619e1-4d41-403a-b8f9-1e9fc46f9ec6" />

### EX-13:If-Else
### code:
```
def even_odd(num):
    if not isinstance(num, int):
        print("Invalid Input")
        return

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = 8
even_odd(num)
```
output:
<img width="640" height="86" alt="image" src="https://github.com/user-attachments/assets/f1955158-9c83-4b98-9a84-54e792b2183b" />

### EX-14:If-Elif-Else
### code:
```
def grade(score):
    if score < 0 or score > 100:
        print("Invalid Score")
        return

    if score >= 80:
        print("Grade A")
    elif score >= 60:
        print("Grade B")
    else:
        print("Grade C")

score = 88
grade(score)
```
### output:
<img width="642" height="82" alt="image" src="https://github.com/user-attachments/assets/d416d27c-773d-427d-808e-e388284303aa" />

### EX-15:Nested If
### code:
```
def login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        print("Blank input")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Invalid User")

user = "admin"
pwd = "pass123"

login(user, pwd)

```
### output:
<img width="611" height="76" alt="image" src="https://github.com/user-attachments/assets/e583448e-e097-4f1e-991f-2a1a437e124c" />

### EX-16:For Loop Basics
### code:
```
def print_numbers(count):

    if count <= 0:
        print("Invalid Count")
        return

    for i in range(count):
        print(i + 1)


print_numbers(5)
```
### output:
<img width="648" height="174" alt="image" src="https://github.com/user-attachments/assets/878ed924-29f0-44cb-b9fb-02902b1beb5f" />

### EX-17:While Loop
### code:
```
def countdown(count):

    if count <= 0:
        print("Invalid Count")
        return

    while count > 0:
        print(count)
        count -= 1


countdown(5)
```
### output:
<img width="675" height="163" alt="image" src="https://github.com/user-attachments/assets/92718348-f739-4734-b845-334f20acafcf" />

### EX-18:Break Statement
### code:
```
def first_even(start, end):

    if start > end:
        print("Invalid Range")
        return

    for i in range(start, end + 1):
        if i % 2 == 0:
            print("First Even Number:", i)
            break


first_even(1, 10)
```
### output:
<img width="612" height="83" alt="image" src="https://github.com/user-attachments/assets/00ee04c5-12cf-4b84-8dff-18bb955065c1" />

### EX-19:Continue Statement
### code:
```
def sum_odd():
    total = 0

    for i in range(10):
        if i % 2 == 0:
            continue

        total += i

    print("Sum of odd numbers:", total)

sum_odd()
```
### output:
<img width="620" height="70" alt="image" src="https://github.com/user-attachments/assets/8ae0986b-22b4-4cba-8f8b-059d95a4ed6a" />

### EX-20:Pass Statement
### code:
```
def future_feature():
    pass


future_feature()

print("Function defined")
```
### output:
<img width="677" height="66" alt="image" src="https://github.com/user-attachments/assets/44626d2e-81ab-416d-967a-3a10b6949a57" />

### EX-21:Consistent Indentation
### code:
```
def check_nested():
    condition1 = True
    condition2 = True

    if condition1:
        if condition2:
            print("Nested")

    print("Program executed successfully")

check_nested()
```
### output:
<img width="655" height="102" alt="image" src="https://github.com/user-attachments/assets/c89620af-03b6-4e5c-9dd8-a2df7561f9bd" />

### EX-22:Comment Usage
### code:
```
def calculate_salary():
    # Base salary
    base = 50000

    # Bonus amount
    bonus = 10000

    # Total salary
    total = base + bonus

    print("Total Salary:", total)

calculate_salary()
```
### output:
<img width="613" height="87" alt="image" src="https://github.com/user-attachments/assets/82e3df1e-47c2-4807-a3d6-605dde9cfd38" />

### EX-23:Import Standard Module
### code:
```
import math

def circle_area(radius):
    if radius <= 0:
        print("Invalid Radius")
        return

    area = math.pi * radius ** 2
    print(f"Area of Circle: {area:.2f}")

circle_area(5)
```
### output:
<img width="609" height="75" alt="image" src="https://github.com/user-attachments/assets/06d593b0-2a05-4fc4-8ace-1596e97cbb52" />

### EX-24:All Import
### code:
```
from math import *

def math_demo(num):
    if num < 0:
        print("Invalid Number")
        return

    print("Square Root:", sqrt(num))
    print("Power:", pow(num, 2))
    print("Pi:", pi)

math_demo(16)
```
output:
<img width="634" height="112" alt="image" src="https://github.com/user-attachments/assets/fbd8afb2-f0cf-4823-9206-23f5f7e0842e" />

### EX-25:Parameters
### code:
```
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid Input"

    return a + b

print("Sum =", add(5, 3))
```
### output:
<img width="641" height="82" alt="image" src="https://github.com/user-attachments/assets/d2be9604-a05a-4e6f-9684-fde1061afb78" />

### EX-26:Multiple Parameters
### code:
```
def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        return "Invalid Input"

    return length * width

print("Area =", rectangle_area(5, 3))
```
### output:
<img width="638" height="78" alt="image" src="https://github.com/user-attachments/assets/f2d4f5d6-f7d7-4d0c-9e0e-99bdb13bc99e" />

### EX-27:Len Function
### code:
```
def string_length(text):
    if not text:
        print("Empty String")
        return

    print("Length =", len(text))

string_length("Python")
```
### output:
<img width="651" height="76" alt="image" src="https://github.com/user-attachments/assets/bf440a47-bb71-4a96-9ba5-8569f74faa65" />

### EX-28:Write to File
### code:
```
def write_file():

    with open("greeting.txt", "w") as file:
        file.write("Hello World")

    print("Data written successfully")


write_file()
```
### output:
<img width="639" height="85" alt="image" src="https://github.com/user-attachments/assets/e8e844c6-a15a-485b-a277-c10538dbc964" />

### EX-29:Read from File
### code:
```
def read_file():

    try:
        with open("greeting.txt", "r") as file:
            content = file.read()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("File not found")


read_file()
```
### output:
<img width="650" height="82" alt="image" src="https://github.com/user-attachments/assets/05f67952-7831-463c-96c3-e562beefe78a" />

### EX-30:Basic Try-Except
#### code:
```
def divide(a, b):

    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")


divide(10, 2)
divide(10, 0)
```
### output:
<img width="634" height="99" alt="image" src="https://github.com/user-attachments/assets/dafa5d87-75ff-4a1b-a410-cbf70e855c5f" />

### EX-31:Create List
### code:
```
def display_cart():
    cart = [100, 250, 75]

    if not cart:
        print("Cart is empty")
        return

    print("Shopping Cart:", cart)

display_cart()
```
### output:
<img width="1020" height="116" alt="image" src="https://github.com/user-attachments/assets/29195f3d-bed0-4f96-81b4-1c91ff24194f" />


### EX-32:Append to List
### code:
```
def add_expense():
    expenses = [1000, 1500, 2000]
    new_expense = 500

    if new_expense <= 0:
        print("Invalid Expense")
        return

    expenses.append(new_expense)
    print("Updated Expenses:", expenses)

add_expense()
```
### output:
<img width="643" height="76" alt="image" src="https://github.com/user-attachments/assets/280bf9fe-310b-4a5c-9e6e-435a3f2fa176" />

### EX-33:Update Dictionary
### code:
```
def merge_employee_data():
    emp1 = {"name": "Supraja", "salary": 75000}
    emp2 = {"department": "IT"}

    emp1.update(emp2)

    print(emp1)

merge_employee_data()
```
### output:
<img width="669" height="81" alt="image" src="https://github.com/user-attachments/assets/29215ee2-e431-4c4a-97a8-90e641cb3f6f" />

### EX-34:Nested Dictionary
### code:
```
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

get_salary(employees, "IT", "Ashwin")
```
### output:
<img width="626" height="72" alt="image" src="https://github.com/user-attachments/assets/56029f54-3df7-4c25-8149-c7b06d62742f" />

### EX-35:Create Tuple
### code:
```
def display_coordinates():
    coordinates = (10, 20)

    if len(coordinates) != 2:
        print("Invalid Coordinates")
        return

    print(f"X = {coordinates[0]}, Y = {coordinates[1]}")

display_coordinates()
```
### output:
<img width="670" height="85" alt="image" src="https://github.com/user-attachments/assets/4278d8f6-17a8-4df8-850d-43ac4cd0c5a7" />

### EX-36:Set Intersection
### code:
```
def common_skills():
    skills1 = {"Python", "Java", "SQL"}
    skills2 = {"Python", "C++", "SQL"}

    common = skills1 & skills2

    print("Common Skills:", common)

common_skills()
```
### output:
<img width="646" height="75" alt="image" src="https://github.com/user-attachments/assets/55c2637b-00c8-4821-85d5-f6ae4d3787fd" />

### EX-37:Multiple Instances
### code:
```
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
```
### output:
<img width="646" height="129" alt="image" src="https://github.com/user-attachments/assets/e9875029-d40d-4bb8-a6a7-5fdc4a3a1f98" />

### EX-38:Method Chaining
### code:
```
class Employee:
    def __init__(self):
        self.salary = 0

    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        return self

    def apply_raise(self, amount):
        self.salary += amount
        return self

    def display(self):
        print("Final Salary:", self.salary)
        return self

Employee().set_salary(50000).apply_raise(5000).display()
```
### output:
<img width="658" height="73" alt="image" src="https://github.com/user-attachments/assets/f4b32a97-ef7a-496e-97f0-47b2f2c7ef4a" />

### EX-39:Polymorphism
### code:
```
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Manager(Employee):
    def work(self):
        print("Manager conducts meetings")

employees = [Developer(), Manager()]

for emp in employees:
    emp.work()
```
### output:
<img width="658" height="94" alt="image" src="https://github.com/user-attachments/assets/e9ba7703-490b-4050-a246-ab3ab331d9ab" />

### EX-40:Class Methods
### code:
```
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split(",")
        return cls(name, int(salary))

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

emp = Employee.from_string("Supraja,75000")
emp.display()
```
### output:
<img width="635" height="98" alt="image" src="https://github.com/user-attachments/assets/ad900748-9c4c-4345-838e-7abc2cb0453a" />

### EX-41:Employee Management System
### code:
```
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
```
### output:
<img width="632" height="111" alt="image" src="https://github.com/user-attachments/assets/6a1a9fdf-f3b6-40a3-9b9a-878de3031c2b" />

### EX-42:Data Analysis Pipeline
### code:
```
import statistics

try:
    with open("sales.txt", "r") as file:
        sales = [float(line.strip()) for line in file]

    print("Mean:", statistics.mean(sales))
    print("Median:", statistics.median(sales))

except FileNotFoundError:
    print("sales.txt not found")
```
### output:
<img width="658" height="100" alt="image" src="https://github.com/user-attachments/assets/fd3bd11b-22a9-4ffd-bff3-b0f9e85851dd" />

### EX-43:Configuration Manager
### code:
```
import configparser

class Config:
    pass

class DatabaseConfig(Config):
    pass

config = configparser.ConfigParser()
config.read("db.ini")

db = config["DATABASE"]

print("Host:", db["host"])
print("User:", db["user"])
print("Database:", db["database"])

```
### output:
<img width="680" height="118" alt="image" src="https://github.com/user-attachments/assets/86f857c0-b127-4fde-b0ba-62926f8869ef" />

### EX-44:CSV Data Processor
### code:
```
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
```
### output:
<img width="702" height="141" alt="image" src="https://github.com/user-attachments/assets/04d64386-8559-4cb5-9cfe-cb654422ba88" />

### EX-45:Expense Tracker
## code:
```
import csv

expenses = {}

with open("expenses.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        category = row["category"]
        amount = float(row["amount"])

        expenses[category] = expenses.get(category, 0) + amount

print("Expense Summary")

for category, total in expenses.items():
    print(category, ":", total)
```
### output:
<img width="656" height="114" alt="image" src="https://github.com/user-attachments/assets/428efff0-dbb7-452e-a88f-dcb49347dca0" />

### EX-46:API Response Handler
## code:
```
import requests

try:
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=11&longitude=78&current_weather=true"
    )

    data = response.json()

    print("Temperature:", data["current_weather"]["temperature"])
    print("Wind Speed:", data["current_weather"]["windspeed"])

except requests.exceptions.RequestException:
    print("Network Error")
```
### output:
<img width="669" height="103" alt="image" src="https://github.com/user-attachments/assets/ab365bde-6b3f-4b76-ac00-2621c22e5f6f" />

### EX-47:Complete Calculator Program
### code:
```
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid Operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

print("Result =", calculate(a, b, op))
```
### output:
<img width="621" height="112" alt="image" src="https://github.com/user-attachments/assets/10cf0ce5-2ee7-42b7-b008-f3d7958e5723" />

### EX-48:Shopping Cart System
## code:
```
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(i.price * i.quantity for i in self.items)

cart = ShoppingCart()

cart.add_item(CartItem("Pen", 10, 2))
cart.add_item(CartItem("Book", 50, 1))

subtotal = cart.calculate_total()
gst = subtotal * 0.18
total = subtotal + gst

print("Subtotal:", subtotal)
print("GST:", gst)
print("Total:", total)
```
### output:
<img width="771" height="118" alt="image" src="https://github.com/user-attachments/assets/94a76929-80d4-4ad7-9093-4bc8fd2921dc" />

### EX-49:Temperature Converter GUI
## code:
```
from tabulate import tabulate

celsius = 25

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

table = [
    ["Celsius", celsius],
    ["Fahrenheit", round(fahrenheit, 2)],
    ["Kelvin", round(kelvin, 2)]
]

print(tabulate(table, headers=["Scale", "Value"]))
```
### output:
<img width="631" height="179" alt="image" src="https://github.com/user-attachments/assets/31331e11-d9ff-4c46-a3b7-4a0798baf96f" />

### EX-50:Backup Utility
## code:
```
import shutil

try:
    shutil.copy("sample.txt", "backup_sample.txt")

    with open("backup.log", "a") as log:
        log.write("sample.txt copied\n")

    print("Backup Completed")

except FileNotFoundError:
    print("File Not Found")

except PermissionError:
    print("Permission Denied")
```
### output:
<img width="631" height="179" alt="image" src="https://github.com/user-attachments/assets/d31cddcc-eec1-452d-ae05-530697e79b05" />

### EX-51:URL Shortener
## code:
```
import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten(self, url):
        short_code = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short_code] = url
        return short_code

    def retrieve(self, short_code):
        return self.urls.get(short_code, "URL not found")

shortener = URLShortener()

url = "https://www.google.com"
code = shortener.shorten(url)

print("Short Code:", code)
print("Original URL:", shortener.retrieve(code))

```
### output:
<img width="706" height="96" alt="image" src="https://github.com/user-attachments/assets/9fb0f4f0-7ea3-440c-9554-ba10f5649b90" />

### EX-52:Gradebook System
## code:
```
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
```
### output:
<img width="661" height="145" alt="image" src="https://github.com/user-attachments/assets/bc6c5f15-f27f-4ade-bb8b-616d07424955" />


### EX-53:Task Scheduler
## code:
```
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

tasks = [
    Task("Project Report", "2026-06-15", 1),
    Task("Assignment", "2026-06-10", 2),
    Task("Presentation", "2026-06-20", 3)
]

tasks.sort(key=lambda task: task.due_date)

print("Task Schedule")

for task in tasks:
    print(
        task.name,
        task.due_date.strftime("%Y-%m-%d"),
        "Priority:",
        task.priority
    )
```
### output:
<img width="737" height="139" alt="image" src="https://github.com/user-attachments/assets/7ef6593d-6387-4abe-9fbc-8c11e7389627" />

### EX-54:Inventory Manager
## code:
```
class Product:
    def __init__(self, name):
        self.name = name

class Perishable(Product):
    pass

class Electronics(Product):
    pass

inventory = {
    "Milk": 5,
    "Laptop": 15,
    "Bread": 3
}

low_stock = {
    item for item, qty in inventory.items()
    if qty < 10
}

print("Inventory Summary")

for item, qty in inventory.items():
    print(item, ":", qty)

print("Low Stock Alerts:", low_stock)
```
### output:
<img width="696" height="174" alt="image" src="https://github.com/user-attachments/assets/fef29b3d-0bfb-46fc-b696-65ff17beac4f" />

### EX-55:Budget Planner
## code:
```
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

food = Category("Food", 5000)
travel = Category("Travel", 3000)
shopping = Category("Shopping", 4000)

food.spent = 4500
travel.spent = 3500
shopping.spent = 2500

categories = [food, travel, shopping]

for category in categories:
    if category.spent > category.limit:
        print(f"Alert: {category.name} budget exceeded!")

labels = [c.name for c in categories]
amounts = [c.spent for c in categories]

plt.pie(amounts, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Budget Usage")
plt.show()

```
### output:
<img width="687" height="90" alt="image" src="https://github.com/user-attachments/assets/28769d1d-ac48-4663-8a78-b0a762d1ee48" />

<img width="797" height="679" alt="image" src="https://github.com/user-attachments/assets/aad489ef-566d-4d13-9988-09503796a280" />


