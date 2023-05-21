def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(dividend, divisor):
    return dividend / divisor


def display(value):
    for item in value:
        print(item)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number? "))
display(operations)
operation = input("Pick an operation from the line above. ")
num2 = int(input("What's the second number? "))
result = operations[operation](num1, num2)
print(f"{num1} {operation} {num2} = {result}")
