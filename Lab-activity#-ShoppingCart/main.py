class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        new_item = Item(name, price)
        self.items.append(new_item)
        print(name, "added to cart.")

    def remove_item(self, name):
        found = False

        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(name, "removed from cart.")
                found = True
                break

        if not found:
            print("Item not found in cart.")

    def view_cart(self):
        if len(self.items) == 0:
            print("\nCart is empty.")
            return

        total = 0
        print("\nItems in cart:")

        for item in self.items:
            print(item.name, "-", item.price)
            total += item.price

        print("Total:", total)

    def checkout(self):
        if len(self.items) == 0:
            print("\nCart is empty.")
            return

        total = 0
        print("\nCheckout items:")

        for item in self.items:
            print(item.name, "-", item.price)
            total += item.price

        print("Total amount:", total)
        print("Thank you for shopping!")

        self.items.clear()

cart = ShoppingCart()

while True:
    print("\nShopping Cart Menu")
    print("1 - Add Item")
    print("2 - Remove Item")
    print("3 - View Cart")
    print("4 - Checkout")
    print("5 - Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.add_item(name, price)

    elif choice == "2":
        name = input("Enter item name to remove: ")
        cart.remove_item(name)

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")