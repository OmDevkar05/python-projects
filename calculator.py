while True:
    a = int(input(" Enter first number : "))
    operation = input("Enter Operator, +, -, *, / : ")
    c = int(input("Enter Second number : "))
    if operation == '+':
        print("Addition of", a, "and", c, "is: ", a + c)
    elif operation == '-':
        print("Subtraction of", a, "and", c, "is: ", a - c)
    elif operation == '*':
        print("Multiplication of", a, "and", c, "is: ", a * c)
    elif operation == '/':
        if c != 0:
            print("Division of", a, "and", c, "is: ", a / c)
        else:
            print("Cannot divide by Zero")
    else:
        print(" ERROR...")
    again = input("Do you want to perform operation again? Type Yes or No :").upper()
    if again != "YES":
        print("Exit...")
        break
