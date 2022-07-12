import os
from item import Item
from color import bcolors


class InputOutput:
    # def __init__(self, user_input, user_output):
    #     self.user_input = user_input
    #     self.user_output = user_output

    def welcome_menu(self):
        print(bcolors.BOLD + bcolors.OKBLUE +
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
        # create the object for the class
        return Item(title, description, style, size, brand, price)

    def display_wardrobe(self, items):
        os.system('clear')
        for item in items:
            item.show_item()
            # get attribute from object

# wrapper method we are in control of user_input
    def user_input(self, message=""):
        return input(message)

    def delete_item_question(self):
        print("Which item do you want to remove by title?:   ")
