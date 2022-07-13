import os
from color import bcolors


class InputOutput:

    def welcome_menu(self):
        print(bcolors.OKBOLD + bcolors.OKBLUE +
              "Welcome to MY WARDROBE. \nPlease select what you would like to do from the following:   " + bcolors.ENDC)
        print(bcolors.OKGREEN +
              "1. Add a new label and item to your wardrobe" + bcolors.ENDC)
        print(bcolors.OKCYAN + "2. Delete an item in you wardrobe" + bcolors.ENDC)
        print(bcolors.OKGREEN + "3. View my wardrobe" + bcolors.ENDC)
        print(bcolors.OKCYAN + "4. Reset your wardrobe" + bcolors.ENDC)
        print(bcolors.OKGREEN + "5. Quit" + bcolors.ENDC)

    def create_item(self):
        os.system('clear')
        title = self.user_input(
            bcolors.OKYELLOW + f"Please enter a title for your item:  " + bcolors.ENDC)
        description = self.user_input(
            bcolors.OKRED + f"Please enter the item description:  " + bcolors.ENDC)
        style = self.user_input(
            bcolors.OKGREEN + f"Please enter the item style:  " + bcolors.ENDC)
        size = self.user_input(
            bcolors.OKCYAN + f"Please enter the item size on tag:  " + bcolors.ENDC)
        brand = self.user_input(
            bcolors.OKBLUE + f"Please enter the item brand:  " + bcolors.ENDC)
        price = self.user_input(
            bcolors.OKYELLOW + f"Please enter the item price:  " + bcolors.ENDC)
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
        print("Which item do you want to remove by title?:   ")

    def reset_wardrobe_question(self):
        print(bcolors.OKBOLD + bcolors.OKRED +
              "Are you sure you want to reset your wardrobe(Y/N)?  \n" + bcolors.ENDC)

    def not_reset_wardrobe(self):
        print("Your wardrobe has not been reset.\n")
