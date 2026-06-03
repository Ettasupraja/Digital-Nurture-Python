class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(i.price * i.quantity for i in self.items)

cart = ShoppingCart()

cart.add_item(CartItem("Pen", 10, 2))
cart.add_item(CartItem("Book", 50, 1))

subtotal = cart.calculate_total()
gst = subtotal * 0.18
total = subtotal + gst

print("Subtotal:", subtotal)
print("GST:", gst)
print("Total:", total)