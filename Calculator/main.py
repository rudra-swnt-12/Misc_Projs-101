from random import choice

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
    "/": divide,
}

# print(operations["*"] (4,9))
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)  #Gives user the list of all symbols
        operation_symbol = input("Pick an operation to carry out: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        #Does the main operation adn shows the operation.

        input(f"Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation.")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() #for recursion.
calculator() #after ending the calculation.






