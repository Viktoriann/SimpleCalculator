from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    should_accumulate = True
    first_number = float(input("What's the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calculation_result = operations[operation_symbol](first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {calculation_result}")
        choice = input(f"Type 'y' to continue calculating with {calculation_result}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            first_number = calculation_result

        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()