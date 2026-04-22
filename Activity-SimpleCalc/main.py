print("====Simple Calculator====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try :
    operation = int(input("Enter choice (1/2/3/4): "))
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: \n")

    if operation == 1:
        result = num1 + num2 
        print(result)
    
    elif operation == 2:
        result = num1 - num2 
        print(result)
    
    elif operation == 3:
        result = num1 * num2 
        print(result)
    
    elif operation == 4:
        if num2 == 0:
            print("Error. Cant be divided by zero.")
        else:
            result = num1 / num2
            print(result)

    else:
        print("Invalid input.")

except ValueError:
    print("Error. Please try again.")