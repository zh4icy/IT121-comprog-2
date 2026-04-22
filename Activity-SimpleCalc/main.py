def calculate(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return None  

print("==== Simple Calculator ====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    operation = int(input("Enter choice (1/2/3/4): "))

    if operation not in [1, 2, 3, 4]:
        print("Invalid choice.")
    else:
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))

        result = calculate(num1, num2, operation)
        print("Result:", result)

except ValueError:
    print("Error. Please enter valid numbers.")