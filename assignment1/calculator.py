Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
operation = input("Enter operation: ")

if operation == "+":
    result = Num1 + Num2
    print("Result: ", result)
elif operation == "-":
    result = Num1 - Num2
    print("Result: ", result)
elif operation == "*":
    result = Num1 * Num2
    print("Result: ", result)
elif operation == "/":
    
    if Num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = Num1 / Num2
        print("Result: ", result)
else:
    print("Invalid operation")