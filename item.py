import os


class Item:
    # never call init, it's the method that sets the inital attrributes to the class
    def __init__(self, title, description, style, size, brand, price):
        self.title = title
        self.description = description  # name value of the attribute
        self.style = style
        self.size = size
        self.brand = brand
        self.price = price

    def show_item(self):
        print(
            f"Title: {self.title}, Description: {self.description}, Style: {self.style}, Size:{self.size}, Brand:{self.brand}, Price: ${self.price}\n\n")


# item1 = Item("comfy jeans", "boyfriend", "jeans", 12, "bottoms", 99.99)
# item1.show_item()
