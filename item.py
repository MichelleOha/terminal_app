import os


class Item:
    # never call init, it's the method that sets the inital attrributes to the class
    def __init__(self, title, description, style, size, category, price):
        self.title = title
        self.description = description  # name value of the attribute
        self.style = style
        self.size = size
        self.category = category
        self.price = price

    def show_item(self):
        print(
            f"{self.title}: {self.description}: {self.style}: {self.size}: {self.category}: ${self.price}")


# item1 = Item("comfy jeans", "boyfriend", "jeans", 12, "bottoms", 99.99)
# item1.show_item()
