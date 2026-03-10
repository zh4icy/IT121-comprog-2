x = 300

print("Find the closest number to", x)

a = int(input("\nEnter your first number (A): "))
b = int(input("Enter your second number (B): "))
c = int(input("Enter your third number (C): "))

diff_a = abs(x - a)
diff_b = abs(x - b)
diff_c = abs(x - c)

if diff_a == diff_b == diff_c:
    print("\nAll numbers are equally close to", x)
elif diff_a <= diff_b and diff_a <= diff_c:
    print("\nLetter A or", a, "is the closest number to", x)
elif diff_b <= diff_a and diff_b <= diff_c:
    print("\nLetter B or", b, "is the closest number to", x)
else:
    print("\nLetter C or", c, "is the closest number to", x)