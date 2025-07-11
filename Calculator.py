# in this file for the first time i'll try to create a calculator


def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        print("Damn your given number, please give something biggar than '0' ")
        return None
    return x / y


def exp(x, y):
    return x**y


print("Wellcome to my new fucking calculator")

count = 0
valid_operator = ["+", "-", "*", "/", "**"]

while True:
    operator = input("\nEnter your operation (+ - * / **) or 'q' to quit: ")
    if operator is "q":
        print(f"Your total operator done: {count}")
        print("Goodbye Bad boyaa")
        break

    if operator not in valid_operator:
        print("Please input any valid opertors (+ - * / **): ")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Please use valid number")
        continue

    if operator == "+":
        print("Result:", sub(num1, num2))
        count += 1

    elif operator == "-":
        print("Result:", sub(num1, num2))
        count += 1

    elif operator == "*":
        print("Result:", mul(num1, num2))
        count += 1

    elif operator == "/":
        print("Result:", div(num1, num2))

    elif operator == "**":
        print("Result:", exp(num1, num2))
        count += 1

    else:
        print("Invalid operator.")
