# WEEK 7 - Simple Money Withdrawal System

balance = 1000  # starting balance

while True:
    print("\n==== MENU ====")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        try:
            amount = float(input("\nEnter amount to withdraw: "))

            if amount > balance:
                print("\nError: \nInsufficient funds!")

                # Options after error
                print("\nWhat would you like to do?")
                print("1. Try again")
                print("2. Check balance")
                print("3. Exit")

                option = input("\nEnter choice: ")

                if option == "1":
                    continue
                elif option == "2":
                    print("\nCurrent balance:", balance)
                elif option == "3":
                    print("\nThank you! Goodbye.")
                    break
                else:
                    print("\nInvalid option.")

            elif amount <= 0:
                print("\nEnter a valid amount.")

            else:
                balance -= amount
                print("\nWithdrawal successful!")
                print("\nRemaining balance:", balance)

        except ValueError:
            print("\nError: Invalid input! Please enter a number.")

    elif choice == "2":
        print("\nCurrent balance:", balance)

    elif choice == "3":
        print("\nThank you! Goodbye.")
        break

    else:
        print("\nInvalid choice. Please try again.")