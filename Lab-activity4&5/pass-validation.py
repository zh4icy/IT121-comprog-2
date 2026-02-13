while True:
    input_pass = input("Enter Password: ")
    
    has_letter = any(chr.isalpha()for chr in input_pass) 
    has_digit = any(chr.isdigit() for chr in input_pass) 

    if has_digit and has_letter:
        print("Password accepted!") 
        break
    else: print("Invalid Password. Please try again.")