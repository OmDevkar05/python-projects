def sum(a, b):
    addition = a + b
    print("Sum is : ", addition)


# a = int(input(" Enter First number : "))
# b = int(input(" Enter Second number : "))
# sum(a,b)

def sub(a, b):
    Subtraction = a - b
    print("Subtraction is : ", Subtraction)


# a = int(input(" Enter First number : "))
# b = int(input(" Enter Second number : "))
# sub(a,b)

def multiplication(a, b):
    Multiplication = a * b
    print("Multiplication is : ", Multiplication)


def division(a, b):
    Divison = a / b
    print("Divison is : ", Divison)


a = int(input(" Enter First number : "))
operation = input("Enter the Operation : '+ , - , * , /' : ")
b = int(input(" Enter Second number : "))

if operation == "+":
    print(sum(a, b))
elif operation == "-":
    print(sub(a, b))
elif operation == "*":
    print(multiplication(a, b))
elif operation == "/":
    print(division(a, b))
else:
    print(" Invalid...")
