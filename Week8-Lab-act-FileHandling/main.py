try:
    file = open("Week8-Lab-act-FileHandling/message.txt", "x")
    print("\nFile created successfully!")
    file.close()
except FileExistsError:
    print("\nError creating file. Try again.")

while True:
    print("\n====Simple Messaging App====\n")
    print("1) Send a message.")
    print("2) View all messages.")
    print("3) Exit program.")

    choice = input("\nEnter your choice: ")

#Option 1 : SENDING A MESSAGE
    if choice == "1":
        message = input("\nEnter message: ")
        try: 
            with open("Week8-Lab-act-FileHandling/message.txt", "a") as file:
                file.write(message + "\n")
            print("\nMessage saved!")
        except Exception: 
            print("\nError writing to file. Try again.")

#Option 2 : VIEW ALL MESSAGES.
    elif choice == "2":
        try:
            with open("Week8-Lab-act-FileHandling/message.txt", "r") as file:
                content = file.read()
                if content == "":
                    print("\nNo messages yet.")
                else:
                    print("\n----Messages----")
                    print(content)
        except Exception :
            print("\nError reading file.")

#Option 3 : EXIT PROGRAM.
    elif choice == "3":
        print("\nExiting program:)...")
        break
    
    else:
        print("\nInvalid choice. Try again.")
