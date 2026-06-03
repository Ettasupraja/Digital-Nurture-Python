from math import *

def math_demo(num):
    if num < 0:
        print("Invalid Number")
        return

    print("Square Root:", sqrt(num))
    print("Power:", pow(num, 2))
    print("Pi:", pi)

math_demo(16)