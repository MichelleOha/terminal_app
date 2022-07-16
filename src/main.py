from read_write import ReadWrite
import os
from input_output import InputOutput


class Main:

    def __init__(self, input_output, read_write):
        self.input_output = input_output
        self.read_write = read_write
        self.running = True

    def app(self):
        while self.running:
            self.input_output.welcome_menu()
        # Here we have a class and method then save it to a variable
        # The method waits for input from user and I capture it in menu_selection and store it
            menu_selection = self.input_output.user_input()
            if menu_selection == "1":  # Add a new label and item to your wardrobe
                os.system('clear')
                # Store info in dictionary, save to json and create an item list
                item = self.input_output.create_item()
                self.read_write.write_item_to_json(item)
            elif menu_selection == "2":
                os.system('clear')
                self.input_output.delete_item_question()
                delete_title = self.input_output.user_input()
                json_list = self.read_write.get_json_list()
                for item in json_list:
                    # Checking if the items name of this iteration is equal to the name we receive
                    if item["title"] == delete_title:
                        # Here we access the list and remove the item
                        json_list.remove(item)
                        break
                self.read_write.write_list_to_json(json_list)
            elif menu_selection == "3":
                os.system('clear')
                json_list = self.read_write.get_json_list()
                self.input_output.display_wardrobe(json_list)
            elif menu_selection == "4":
                os.system('clear')
                self.input_output.reset_wardrobe_question()
                delete_wardrobe = self.input_output.user_input()
                # For wardrobe_reset_question in self.input_output:
                # Checks if the item's name of this iteration is equal to the name we receive
                if delete_wardrobe.lower() == "y":
                    # Access wardrobe and remove the it
                    self.read_write.reset_json()
                else:
                    os.system('clear')
                    self.input_output.not_reset_wardrobe()
            elif menu_selection == "5":
                self.running = False


# This is Dependance Injection - data base class - InputOutput ReadWrite
main = Main(InputOutput(), ReadWrite(('list.json')))
main.app()
