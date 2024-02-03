def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}


def calculator():
    print("Welcome to calculator program...!!")
    num1 = float(input("What's the first number: "))
    should_continue = True
    while should_continue == True:
        for key in operations:
            print(key)
        op_symbol = input("Select the Opertion you want to perform: ")
        op_symbol_func = operations[op_symbol]
        num2 = float(input("What's the next number: "))
        answer = op_symbol_func(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
        usr_input = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start new calculation, or 'exit' to exit the calculator program: ")
        if usr_input == 'y':
            num1 = answer
        elif usr_input == 'n':
            calculator()
        else:
            should_continue = False

calculator()