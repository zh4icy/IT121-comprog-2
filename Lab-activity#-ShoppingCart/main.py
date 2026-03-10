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