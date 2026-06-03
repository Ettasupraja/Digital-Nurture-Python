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