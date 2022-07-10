import os
from item import Item
from input_output import InputOutput


class Main:

    def __init__(self, input_output):
        self.input_output = input_output
        self.running = True
        self.items = []  # empty list so we can add to it with user input

    def app(self):

        while self.running:
            self.input_output.welcome_menu()
            # class and method then save it to a variable
            # method waits for input from user and I capture it menu_selection and store it
            menu_selection = self.input_output.user_input()
            if menu_selection == "1":  # Add a new label and item to your wardrobe
                os.system('clear')
                item = self.input_output.create_item()  # store info
                self.items.append(item)
            elif menu_selection == "2":
                os.system('clear')
                self.input_output.delete_item_question()
                delete_title = self.input_output.user_input()
                for item in self.items:
                    # checking if the items name of this iteration is equal to the name we receive
                    if item.title == delete_title:
                        # access to the list and remove the item
                        self.items.remove(item)
                        break
            elif menu_selection == "3":
                os.system('clear')
                self.input_output.display_wardrobe(self.items)
            elif menu_selection == "4":
                os.system('clear')
                self.items = []
            elif menu_selection == "5":
                self.running = False


# dependance injection - data base class - InputOutput
main = Main(InputOutput())
main.app()
