print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply") 


try: 
        
    operation = int(input("\nEnter choice (1/2/3/4): "))

    if operation < 1 or operation > 4:
        print("Invalid operation choice.")
        exit()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == 1:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == 3:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif operation == 4:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

except ValueError: 
    print("Invalid input. Please enter numbers only.")