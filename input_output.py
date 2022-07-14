import os
from color import Colors


# def get_a_float(prompt):
# Repeatedly asks the user for a number until they give an input that can be converted to an integer. Returns an int.
#price = None

#result = None
# while result is None:
#     try:
#         result = int(input(prompt))
#     except ValueError:
#         print("That wasn't a numeric value, please re-enter the price.")
# return result


class InputOutput:

    def welcome_menu(self):
        print(Colors.BOLD + Colors.PURPLE +
              "Welcome to MY WARDROBE. \nPlease select what you would like to do from the following:   " + Colors.END)
        print(Colors.GREEN +
              "1. Add a new label and item to your wardrobe" + Colors.END)
        print(Colors.BLUE + "2. Delete an item in you wardrobe" + Colors.END)
        print(Colors.GREEN + "3. View my wardrobe" + Colors.END)
        print(Colors.BLUE + "4. Reset your wardrobe" + Colors.END)
        print(Colors.GREEN + "5. Quit" + Colors.END)

    def create_item(self):
        os.system('clear')
        title = self.user_input(
            Colors.YELLOW + f"Please enter a title for your item:  " + Colors.END)
        description = self.user_input(
            Colors.RED + f"Please enter the item description:  " + Colors.END)
        style = self.user_input(
            Colors.GREEN + f"Please enter the item style:  " + Colors.END)
        size = self.user_input(
            Colors.BLUE + f"Please enter the item size on tag:  " + Colors.END)
        brand = self.user_input(
            Colors.PURPLE + f"Please enter the item brand:  " + Colors.END)
        #    while price is None:
        #         try:
        # while result is None:
        #     try:
        #         price = float(self.user_input(
        #             Colors.YELLOW + f"Please enter the item price: $  " + Colors.END))
        #         result = int(input())
        #     except ValueError:
        #         print("That wasn't a numeric value, please re-enter the price.")
        #     return result
        price = self.user_input(
            Colors.YELLOW + f"Please enter the item price: $  " + Colors.END)
        # price = get_a_float
        # except ValueError:
        #     print("Please enter a valid numeric price.\n")
        return {
            "title": title,
            "description": description,
            "style": style,
            "size": size,
            "brand": brand,
            "price": price,
        }

    def display_wardrobe(self, items):
        os.system('clear')
        for item in items:
            print(f"Title: {item['title']}, Description: {item['description']}, Style: {item['style']}, Size: {item['size']}, Brand: {item['brand']}, Price: ${item['price']}\n\n")
           # get attribute from object

# wrapper method we are in control of user_input
    def user_input(self, message=""):
        return input(message)

    def delete_item_question(self):
        print(Colors.BOLD + Colors.YELLOW +
              "Which item do you want to remove by title?:   \n" + Colors.END)

    def reset_wardrobe_question(self):
        print(Colors.BOLD + Colors.RED +
              "Are you sure you want to reset your wardrobe(Y/N)?  \n" + Colors.END)

    def not_reset_wardrobe(self):
        print(Colors.BOLD + Colors.BLUE +
              "Your wardrobe has not been reset.\n" + Colors.END)
