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
exit_calculator = False
num1 = float(input("What's the first number? "))
display(operations)
while not exit_calculator:
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    result = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    another_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ").lower()
    if another_calculation == 'n':
        exit_calculator = True
    else:
        num1 = result

