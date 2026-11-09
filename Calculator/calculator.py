# Simple Calculator (No UI)

def add(x ,y) -> int:
    z = x + y
    return print(z)

def subtract(x ,y) -> int:
    z = x - y
    return print(z)
 
def multiply (x, y) -> int:
    z = x * y
    return print(z)

def divide (x, y) -> int:
    z = x / y
    return print(z)

while True:
    try:
        num1 = int(input("Enter number: "))
        operator = input("Enter operator: ")
        num2 = int(input("Enter number: "))

        if operator == '+':
            add(num1, num2)
        elif operator == '-':
            subtract(num1, num2)
        elif operator == '*':
            multiply(num1, num2)
        elif operator == '/':
            divide(num1, num2)
        elif operator != '+' or '-' or '*' or '/':
            print("Enter a valid operator")
    except ValueError:
        print("That is not a number, enter a nummber")
