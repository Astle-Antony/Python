from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

add = add
subtract = subtract
multiply = multiply
divide = divide

operator =  {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
while True:
    first_number = int(input("Enter the first number: "))
    user_wants_to_continue = True
    while user_wants_to_continue:
        operation = input("Enter the operation: '+', '-', '*', '/' ")
        second_number = int(input("Enter the second number: "))
        answer = operator[operation](first_number, second_number)

        user_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
        if user_continue == "y":
            first_number = answer
            user_wants_to_continue = True
        else:
            user_wants_to_continue = False




