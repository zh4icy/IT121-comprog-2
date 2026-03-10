user_list = []

while True:
    print("\n=====MENU=====")
    print("\n1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    
    choice = input("\nEnter choice: ")

    if choice == "1":
        if len(user_list) == 0:
            print("No Users Found")
        else: 
            print("User List:")
            for i in range(len(user_list)):
                print(i, "-", user_list[i])
        
    elif choice == "2":
        username = input("\nEnter new User: ")
        user_list.append(username)
        print("User added successfully!")
        
    elif choice == "3":
        if len(user_list) == 0:
            print("No Users to update.")
        else: 
            for i in range(len(user_list)):
                print(i, "-", user_list[i])
                
            index = int(input("Enter index number to update: "))
            
            if 0 <= index < len(user_list):
                new_name = input("\nEnter new username: ")
                user_list[index] = new_name
                print("User updated successfully!")
            else:
                print("Invalid index")
                
    elif choice == "4":
        if len(user_list) == 0:
            print("No users to delete.")
        else:
            for i in range(len(user_list)):
                print(i, "-", user_list[i])
                
            index = int(input("Enter index number to delete: "))
            
            if 0 <= index < len(user_list):
                user_list.pop(index)
                print("User deleted successfully!")
            else:
                print("Invalid index.")
                
    elif choice == "5":
        print("Exiting Program :)...")
        break

    else:
        print("Invalid Choice. Please try again.")
