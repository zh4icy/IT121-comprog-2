def find_largest(a, b, c):
    if a >= b and a >= c:
        print("Letter A is the largest number with a value of", a)
    elif b >= a and b >= c:
        print("Letter B is the largest number with a value of", b)
    else:
        print("Letter C is the largest number with a value of", c)

num_1 = int(input("Enter your first number (A): "))
num_2 = int(input("Enter your second number (B): "))
num_3 = int(input("Enter your third number (C): "))

find_largest(num_1, num_2, num_3)