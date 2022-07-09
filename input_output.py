import os


class InputOutput:
    def __init__(self, user_input, user_output):
        self.user_input = user_input
        self.user_output = user_output

    def welcome_menu():
        print("Welcome to My Wardrobe. Please select what you would like to do from the following:   ")
        print("1. Add a new label and item to your wardrobe")
        print("2. Updated items in your wardrobe")
        print("3. Delete an item in you wardrobe")
        print("4. View my wardrobe")
        print("5. Reset your wardrobe")
        print("6. Quit")

    def create_item():
        os.system('clear')
        title = input(f"Please enter a title for your item:  ")
        description = input(f"Please enter the item description:  ")
        style = input(f"Please enter the item style:  ")
        size = (f"Please enter the item size on tag:  ")
        category = input(f"Please enter the item category:  ")
        price = input(f"Please enter the item price:  ")
        return {
            "title": title,
            "description": description,
            "style": style,
            "size": size,
            "category": category,
            "price": price,
        }
